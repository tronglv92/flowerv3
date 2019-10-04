from rest_framework.response import Response


def CustomError(message=None, code=None):
    errors = [{"errorCode": code,
              "errorMessage": message}]
    return errors;
