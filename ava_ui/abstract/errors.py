from logging import getLogger

from django.shortcuts import render

log = getLogger(__name__)


class ErrorStatus():
    PERMISSION_DENIED = 'Permission Denied'
    NOT_AUTHENTICATED = 'Authentication Failure'
    UNKNOWN_ERROR = 'Unknown Error'
    SERVER_ERROR = 'Server Error'
    NOT_FOUND = 'Not Found'

    ERROR_TYPES = {
        PERMISSION_DENIED: 'You do not have permission to do this',
        NOT_AUTHENTICATED: 'You must be logged in to do this',
        UNKNOWN_ERROR: 'An error has occurred',
        SERVER_ERROR: 'A server error has occurred',
        NOT_FOUND: 'Still haven\'t found what you\'re looking for',
    }

    ERROR_TEMPLATES = {
        PERMISSION_DENIED: 'error/permission_denied.html',
        NOT_AUTHENTICATED: 'error/unauthenticated.html',
        UNKNOWN_ERROR: 'error/generic_error.html',
        SERVER_ERROR: 'error/generic_error.html',
        NOT_FOUND: 'error/generic_error.html',
    }


def get_display_message(error_type):
    if error_type in ErrorStatus.ERROR_TYPES:
        return ErrorStatus.ERROR_TYPES[error_type]
    else:
        return ErrorStatus.ERROR_TYPES[ErrorStatus.UNKNOWN_ERROR]


def handle_error(request,
                 status_code=ErrorStatus.UNKNOWN_ERROR,
                 error_message='Unknown Error'):

    if status_code not in ErrorStatus.ERROR_TYPES:
        if status_code in [401, 403]:
            status_code = ErrorStatus.PERMISSION_DENIED

        if status_code in [404, ]:
            status_code = ErrorStatus.NOT_FOUND
        if status_code in [500, ]:
            status_code = ErrorStatus.SERVER_ERROR
        else:
            status_code = ErrorStatus.UNKNOWN_ERROR

    context = {}
    context['status_code'] = status_code
    context['error_message'] = get_display_message(error_type=status_code)

    log.error("Handle_Error:: [" + str(status_code) + "] with message: " + str(error_message))

    template_name = ErrorStatus.ERROR_TEMPLATES[status_code]

    if status_code in [ErrorStatus.PERMISSION_DENIED, ErrorStatus.NOT_AUTHENTICATED]:
        from ava_ui.accounts.views import logout_ui
        return logout_ui(request)
    else:
        return render(request, template_name, context=context)
