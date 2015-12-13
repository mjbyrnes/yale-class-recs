from django.http import HttpResponse


def index(request):
    return HttpResponse("Our class recommendations app.")