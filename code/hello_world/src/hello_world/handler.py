
def lambda_handler(event, context):
    """
    AWS Lambda handler that returns a simple Hello, World! message.

    Args:
        event (dict): Event data passed by Lambda.
        context (LambdaContext): Runtime information.

    Returns:
        dict: Response with status code and body message.
    """
    return {
        "statusCode": 200,
        "body": "Hello, World!"
    }
