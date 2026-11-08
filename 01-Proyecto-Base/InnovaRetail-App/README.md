# InnovaRetail API – Proyecto Final EID1030

Aplicación base para implementar un flujo DevSecOps integrado.

## Endpoints

| Método | Ruta | Uso |
|---|---|---|
| GET | `/` | Información del servicio |
| GET | `/health` | Health check |
| GET | `/products` | Productos simulados |
| GET | `/orders` | Pedidos simulados |
| GET | `/stats` | Resumen operativo |
| GET | `/metrics` | Métricas Prometheus |
| GET | `/simulate-error` | Generación controlada de error HTTP 500 |

## Ejecución local

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
pip install -r requirements.txt
pytest -v
python app.py
```

## Docker

```bash
docker build -t innovaretail-api:2.0 .
docker run --rm -p 5000:5000 innovaretail-api:2.0
```

## Trabajo solicitado

El equipo debe integrar y demostrar:

- GitLab y Merge Requests.
- Pipeline CI/CD.
- Docker y Kubernetes.
- Trivy.
- Prometheus y Grafana.
- Terraform o Ansible.
- Troubleshooting.
- Evidencias organizadas.

Consulte el expediente técnico y el registro de incidencias incluidos en el kit.
