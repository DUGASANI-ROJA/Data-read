import json

from django.shortcuts import render
from django.http import HttpResponse

from .sample import get_source
from .models import Employee, ActivityPeriods

# Create your views here.


def index(request):
    employee = Employee.objects.all()
    return render(request, 'api/index.html', {"employee_list": employee})


def read_data_from_file(request):

    get_source('api/json_data_file')

    return HttpResponse("success")
