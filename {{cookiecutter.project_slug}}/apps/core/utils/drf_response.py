from rest_framework.response import Response
from rest_framework import status


class APIResponse:
    @staticmethod
    def success(data=None, message=None, status_code=status.HTTP_200_OK):
        response = {
            'success': True,
            'data': data
        }

        if message:
            response['message'] = message

        return Response(response, status=status_code)

    @staticmethod
    def error(message, status_code=status.HTTP_400_BAD_REQUEST, errors=None):
        response = {
            'success': False,
            'message': message
        }

        if errors:
            response['errors'] = errors

        return Response(response, status=status_code)