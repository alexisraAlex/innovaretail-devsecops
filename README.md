# InnovaRetail: demostración DevSecOps

Proyecto de portafolio que reúne una aplicación Flask, automatización CI, contenedores, manifiestos Kubernetes, infraestructura Terraform y monitoreo con Prometheus/Grafana.

## Publicación segura

La copia de portafolio no incluye historial Git, entornos virtuales, estado local de Terraform, credenciales, documentos del cliente ni capturas de evidencia. Los valores de ejemplo son marcadores; configura secretos en el entorno o en el almacén de secretos de CI.

## Aplicación

Consulta `01-Proyecto-Base/InnovaRetail-App/README.md` y su `requirements.txt`. Para Grafana, define `GRAFANA_ADMIN_PASSWORD` localmente antes de levantar Docker Compose. No subas un archivo `.env` real.

## Infraestructura

Los archivos de Terraform y Kubernetes son ejemplos de configuración. Revisa los valores del entorno y define secretos fuera del repositorio antes de desplegar.