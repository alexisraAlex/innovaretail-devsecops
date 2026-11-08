resource "local_file" "environment_config" {
  filename = "${path.module}/generated/${var.environment}.env"
  content  = <<-EOT
APP_ENV=${var.environment}
TEAM_NAME=${var.team_name}
APP_VERSION=2.0.0
EOT
}
