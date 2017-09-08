import json
import logging

import requests


SUCCESS = "SUCCESS"
FAILED = "FAILED"

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def send(event, context, response_status, reason=None, response_data=None, physical_resource_id=None):
    response_data = response_data or {}
    response_body = json.dumps(
        {
            'Status': response_status,
            'Reason': reason or "See the details in CloudWatch Log Stream: " + context.log_stream_name,
            'PhysicalResourceId': physical_resource_id or context.log_stream_name,
            'StackId': event['StackId'],
            'RequestId': event['RequestId'],
            'LogicalResourceId': event['LogicalResourceId'],
            'Data': response_data
        }
    )
    headers = {
        'Content-Type': '',
        'Content-Length': len(response_body)
    }
    try:
        response = requests.put(url=event['ResponseURL'], data=response_body, headers=headers)
        logger.debug("Status code: {}".format(response.status_code))
        logger.debug("Status message: {}".format(response.text))
        return True
    except Exception as exc:
        logger.error("Failed executing HTTP request: {}".format(exc))
        return False
