from django.shortcuts import render
from rest_app.models import *
from rest_app.serilizers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


# Create your views here.


def single_stud(request, pk):
    print(("in single_stud API "))
    stud_obj = Student.objects.get(id=pk)    #-----complex datatype
    python_obj = StudentSerializer(stud_obj)  #---cmoplex data type to navite python data type
    json_data = JSONRenderer().render(python_obj.data)    #---python to json
    return HttpResponse(json_data, content_type='application/json')  #--- content_type use to said httpresponce to pass out put in the json 




