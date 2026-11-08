# Kubernetes

Revise los manifiestos antes de aplicarlos.

```bash
kubectl apply -k .
kubectl get all -n innovaretail
kubectl describe deployment innovaretail-api -n innovaretail
kubectl logs -n innovaretail deployment/innovaretail-api
```

El equipo debe sustituir el secreto demostrativo, validar el acceso y documentar una
estrategia básica de rollback.
