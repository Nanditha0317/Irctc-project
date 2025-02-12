import boto3

# Initialize AWS Lambda client
lambda_client = boto3.client('lambda')

# Update function configuration
response = lambda_client.update_function_configuration(
    FunctionName='<your-function-name>',
    Runtime='python3.9'
)

print("Lambda runtime updated:", response)

