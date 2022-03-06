from django.shortcuts import render
from rest_app.models import *
from rest_app.serilizers import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def single_stud(request, pk):
    print(("in single_stud API "))
    stud_obj = Student.objects.get(id=pk)    #-----complex datatype
    python_obj = StudentSerializer(stud_obj)  #---cmoplex data type to navite python data type
    json_data = JSONRenderer().render(python_obj.data)    #---python to json
    return HttpResponse(json_data, content_type='application/json')  #--- content_type use to said httpresponce to pass out put in the json 


def all_stud(request):
    print(" In all_stud API")
    studs_obj = Student.objects.all()
    python_obj = StudentSerializer(studs_obj, many=True)
    json_data = JSONRenderer().render(python_obj.data)
    return HttpResponse(json_data, content_type='application/json')

import io


@csrf_exempt
def create_data(request):
    if request.method == 'POST':
        # print(request.body)
        bytes_data = request.body
        streamed_data = io.BytesIO(bytes_data)
        python_data = JSONParser().parse(streamed_data)
        # print(python_data)
        ser = StudentSerializer(data=python_data)
        print(ser)
        if ser.is_valid():
            ser.save()   #----call create_method of StudentSerializer
            msg = {"msg" : "data created successfully....!"}
            res = JSONRenderer().render(msg)
        return HttpResponse(res, content_type='application/json')
    else:
        msg = {"error" : "Only post request_accepted....!"}
        res = JSONRenderer().render(msg)
        return HttpResponse(res, content_type='application/json')






