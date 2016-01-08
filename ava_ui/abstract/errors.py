from logging import getLogger

from django.shortcuts import render

log = getLogger(__name__)


class ErrorStatus():
    PERMISSION_DENIED = 0
    NOT_AUTHENTICATED = 1
    UNKNOWN_ERROR = 2
    SERVER_ERROR = 3
    NOT_FOUND = 4

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

    def get_display_message(self, error_type):
        if error_type in self.ERROR_TYPES:
            return self.ERROR_TYPES[error_type]
        else:
            return self.ERROR_TYPES[self.UNKNOWN_ERROR]


def handle_error(request,
                 status_code=ErrorStatus.UNKNOWN_ERROR,
                 error_message='Unknown Error',
                 context={}):

    if status_code in [401, 403]:
        status_code = ErrorStatus.PERMISSION_DENIED
    if status_code in [404, ]:
        status_code = ErrorStatus.NOT_FOUND
    if status_code in [500, ]:
        status_code = ErrorStatus.SERVER_ERROR

    context['status_code'] = status_code
    context['error_message'] = ErrorStatus.get_display_message(status_code)

    log.error("Handle_Error:: [" + str(status_code) + "] with message: " + str(error_message))

    template_name = ErrorStatus.ERROR_TEMPLATES[status_code]

    return render(request, template_name, context=context)
