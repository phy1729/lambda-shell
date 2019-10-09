variable "name" {
  type        = string
  description = "Name to use in created resources."
  default     = "lambdashell"
}

variable "policies" {
  type        = set(string)
  description = "Set of AWS Managed policy names to attach to the role."
  default     = []
}
