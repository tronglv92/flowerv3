from rest_framework.response import Response


def CustomResponse(data=None, errors=None,debug=None,status=None, template_name=None, headers=None, exception=False,
                   content_type=None):
    # if isinstance(data, dict) and next(iter(data)) == 'success':
    #     return Response(data, status=status, template_name=template_name, headers=headers, exception=exception,
    #                     content_type=content_type)

    if data is not None:
        tmpData = {}
        tmpData['error'] = False
        tmpData['data'] = data
        tmpData['errors'] = None
        tmpData['debug'] = debug
        return Response(tmpData,status=status, template_name=template_name, headers=headers, exception=exception,
                        content_type=content_type)
    elif errors is not None:
        tmpData = {}
        tmpData['error'] = True
        tmpData['data'] = None
        tmpData['errors'] = errors
        tmpData['debug'] = debug
        return Response(tmpData,status=status, template_name=template_name, headers=headers, exception=exception,
                        content_type=content_type)
