from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse

# Create your views here.


def listt(request):
    return HttpResponse("<h1><a href='/admin'>Admin</a></h1>"+"<br>"+
                        "<h1><a href='/student'>Student</a></h1>"+"<br>"+
                        "<h1><a href='/employee'>Employee</a></h1>")