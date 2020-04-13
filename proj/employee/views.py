from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse

# Create your views here.


def listt(request):
    return HttpResponse("hello")