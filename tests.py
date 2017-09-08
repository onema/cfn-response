import mock
from unittest import TestCase
from .cfnresponse import send


class GenericObject(object):
    def __init__(self, parameters):
        self._parameters = parameters

    def __getattr__(self, name):
        value = self._parameters.get(name, False)
        if not value:
            raise ValueError(f'The value "{name}" is not valid')
        return value


class TestCfnResponse(TestCase):
    @staticmethod
    def _event():
        return {
            'StackId': 'stack_id',
            'RequestId': 'request_id',
            'LogicalResourceId': 'logical_resource_id',
            'ResponseURL': 'http://localhost/response'
        }

    @staticmethod
    def _context():
        obj = GenericObject({'log_stream_name': 'log_stream_name'})
        return obj

    @mock.patch('requests.put')
    def test_cfn_send_success(self, requests_mock):

        # Arrange
        requests_mock.return_value.status_code = 200
        requests_mock.return_value.text = 'OK'

        # Act
        response = send(
            event=self._event(),
            context=self._context(),
            response_status='response_status',
            response_data='response_data',
        )

        # Assert
        self.assertTrue(response)

    @mock.patch('requests.put', mock.Mock(side_effect=Exception()))
    def test_cfn_send_error(self):

        # Arrange - Act
        response = send(
            event=self._event(),
            context=self._context(),
            response_status='response_status',
            response_data='response_data',
        )

        # Assert
        self.assertFalse(response)
