import os
import time
from flask import Flask, jsonify, request, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "2.0.0")
APP_ENV = os.getenv("APP_ENV", "development")
APP_NAME = os.getenv("APP_NAME", "InnovaRetail API")

REQUEST_COUNT = Counter(
    "innovaretail_http_requests_total",
    "Cantidad total de solicitudes HTTP",
    ["method", "endpoint", "status"],
)
REQUEST_LATENCY = Histogram(
    "innovaretail_http_request_duration_seconds",
    "Duración de las solicitudes HTTP",
    ["endpoint"],
)

PRODUCTS = [
    {"id": 1, "name": "Laptop Pro 14", "stock": 12, "price": 899.99},
    {"id": 2, "name": "Monitor 24", "stock": 25, "price": 179.50},
    {"id": 3, "name": "Teclado Mecánico", "stock": 40, "price": 69.90},
]

ORDERS = [
    {"id": 1001, "customer": "Cliente A", "status": "processing", "total": 969.89},
    {"id": 1002, "customer": "Cliente B", "status": "completed", "total": 179.50},
]

@app.before_request
def start_timer():
    request._start_time = time.perf_counter()

@app.after_request
def observe_request(response):
    elapsed = time.perf_counter() - getattr(request, "_start_time", time.perf_counter())
    endpoint = request.path
    REQUEST_COUNT.labels(request.method, endpoint, response.status_code).inc()
    REQUEST_LATENCY.labels(endpoint).observe(elapsed)
    return response

@app.get("/")
def home():
    return jsonify({
        "service": APP_NAME,
        "message": "Plataforma de comercio electrónico InnovaRetail",
        "version": APP_VERSION,
        "environment": APP_ENV,
    }), 200

@app.get("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "innovaretail-api",
        "version": APP_VERSION,
    }), 200

@app.get("/products")
def products():
    return jsonify({"products": PRODUCTS, "total": len(PRODUCTS)}), 200

@app.get("/orders")
def orders():
    return jsonify({"orders": ORDERS, "total": len(ORDERS)}), 200

@app.get("/stats")
def stats():
    return jsonify({
        "products": len(PRODUCTS),
        "orders": len(ORDERS),
        "environment": APP_ENV,
        "version": APP_VERSION,
    }), 200

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@app.get("/simulate-error")
def simulate_error():
    """Endpoint académico para generar un error observable y practicar troubleshooting."""
    return jsonify({
        "error": "simulated_failure",
        "message": "Incidente controlado para práctica de observabilidad",
    }), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "not_found", "message": "El recurso solicitado no existe"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
