from diango.http import HttpResponse
from diango.shortcuts import redirect


def index(request):
    return HttpResponse('index');
