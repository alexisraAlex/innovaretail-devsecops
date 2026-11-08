from app import app

def client():
    app.config["TESTING"] = True
    return app.test_client()

def test_home():
    response = client().get("/")
    assert response.status_code == 200
    assert response.get_json()["service"] == "InnovaRetail API"

def test_health():
    response = client().get("/health")
    data = response.get_json()
    assert response.status_code == 200
    assert data["status"] == "healthy"

def test_products():
    response = client().get("/products")
    data = response.get_json()
    assert response.status_code == 200
    assert data["total"] == 3

def test_orders():
    response = client().get("/orders")
    data = response.get_json()
    assert response.status_code == 200
    assert data["total"] == 2

def test_metrics():
    response = client().get("/metrics")
    assert response.status_code == 200
    assert b"innovaretail_http_requests_total" in response.data

def test_simulated_error():
    response = client().get("/simulate-error")
    assert response.status_code == 500

def test_not_found():
    response = client().get("/no-existe")
    assert response.status_code == 404
