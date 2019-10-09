# lambda-shell

lambda-shell is a service that runs in AWS lambda to provide an alternative means of API access.

## Getting Started

To deploy the lambda and setup the API gateway, run `terraform apply` or include this module in a your own terraform deployment.

To interact with the lambda, run `./shell.py` which will start an interactive shell similar to running aws cli commands. However the service name, action, and flags formatting matches the boto3 interface not the regular cli interface i.e. `s3 list_objects --Bucket foo` not `s3api list-objects --bucket foo`.

By default the role assumed by the lambda has no privileges. Policies may be attached to the role by defining the `policies` input variable. For example `terraform.tfvars` could contain
```
policies = [
  "job-function/ViewOnlyAccess",
]
```
