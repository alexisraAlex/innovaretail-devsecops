# Comandos sugeridos para Trivy

```bash
trivy fs --severity HIGH,CRITICAL .
trivy image --severity HIGH,CRITICAL innovaretail-api:2.0
trivy config 04-Infraestructura/kubernetes
```

El reporte debe incluir: hallazgo, severidad, componente afectado, decisión y evidencia.
