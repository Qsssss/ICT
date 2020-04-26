from django.http.request import HttpRequest
import json
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from student.models import Blank


def menu(request):
    return HttpResponse("<h3><a href='/student/private'>Private data</a></h3>"+
                        "<h3><a href='/student/app'>Application</a></h3>" +
                        "<h3><a href='/student/get_card'>Get Card</a></h3>" +
                        "<h3><a href='/student/registration'>Registration</a></h3>" +
                        "<h3><a href='/student/academic'>Academic mobility</a></h3>" +
                        "<h3><a href='/student/payment'>Pay</a></h3>" +
                        "<h3><a href='/student/answers'>Answers</a></h3>")


def private_data(request):
    return HttpResponse('')


def application(request):
    return HttpResponse("<a href='/status'>Status</a>"+"<br>"+
                        "<a href='/f'>Blank</a>")


def status(request):
    return HttpResponse('')


def get_card(request):
    return HttpResponse('')


def registration(request):
    return HttpResponse('')


def academic_mobility(request):
    return HttpResponse('')


def payment(request):
    return HttpResponse('')


def answers(request):
    return HttpResponse('')


def categories_list(request):
    if request.method == 'GET':
        categories = Blank.objects.all()
        categories_json = [category.short() for category in categories]
        return JsonResponse(categories_json, safe=False)
    elif request.method == 'POST':
        request_body = json.loads(request.body)
        category = Blank.objects.create(firstName=request_body.get('name', 'default name'))
        return JsonResponse(category.to_json())

