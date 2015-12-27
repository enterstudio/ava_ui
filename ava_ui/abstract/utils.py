import logging

from django.shortcuts import render, redirect

log = logging.getLogger(__name__)


def handle_error(request, status_code):
    log.debug("Called handle_error with status code :: " + str(status_code))
    if status_code is '401' or '403':
        return redirect('login')
    else:
        return render(request, 'error/generic_error.html')
