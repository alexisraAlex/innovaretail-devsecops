# Observabilidad

## Evidencias obligatorias

1. Prometheus muestra el target `innovaretail-api` en estado UP.
2. Consulta de `innovaretail_http_requests_total`.
3. Dashboard Grafana importado.
4. Generación de tráfico normal y del error controlado `/simulate-error`.
5. Interpretación de disponibilidad, tráfico, errores y latencia.
6. Uso de `kubectl logs` y `kubectl describe`.
7. Conclusión sobre qué acción tomar antes de modificar el sistema.

## Acceso local sugerido

- API: http://localhost:5000
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000
- Usuario demostrativo de Grafana: admin
- Clave demostrativa: admin

Cambie la clave al iniciar y no utilice credenciales reales en el repositorio.
