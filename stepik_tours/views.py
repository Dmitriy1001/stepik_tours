from django.http import HttpResponseNotFound, HttpResponseServerError


def page_not_found(request, exception):
    return HttpResponseNotFound('Error 404. Page not found...')


def internal_server_error(requset):
    return HttpResponseServerError('Error 500. Server error')
