output "invoke_url" {
  value       = aws_api_gateway_stage.main.invoke_url
  description = "The URL to invoke the API pointing to the stage."
}

output "role_arn" {
  value       = aws_iam_role.main.arn
  description = "ARN of the role the lambda will assume."
}

output "shell_endpoint" {
  value       = "${aws_api_gateway_stage.main.invoke_url}${aws_api_gateway_resource.main.path}"
  description = "Full URL to invoke the shell."
}
