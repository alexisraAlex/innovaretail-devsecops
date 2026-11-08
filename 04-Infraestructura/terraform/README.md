# Terraform

Esta configuración genera un archivo de configuración reproducible para el ambiente.

```bash
terraform init
terraform fmt
terraform validate
terraform plan -var-file="terraform.tfvars"
terraform apply -var-file="terraform.tfvars"
```

Copie `terraform.tfvars.example` como `terraform.tfvars` y personalice el equipo.
