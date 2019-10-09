"""Run AWS command."""
import json

import boto3


def handler(event, _):
    """Run AWS command."""
    req = json.loads(event['body'])
    return {
        'statusCode': 200,
        'body': json.dumps(getattr(boto3.client(**req['client_args']),
                                   req['action'])(**req.get('args', {})),
                           default=str)
    }
