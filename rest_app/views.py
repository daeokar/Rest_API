from django.shortcuts import render
from rest_app.models import *
from rest_app.serilizers import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
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


def common_lines(request):
    bytes_data = request.body
    streamed_data = io.BytesIO(bytes_data)  #----json data
    python_dict = JSONParser().parse(streamed_data)
    return python_dict

@csrf_exempt
def create_data(request):
    if request.method == 'POST':
        # print(request.body)
        # bytes_data = request.body
        # streamed_data = io.BytesIO(bytes_data)
        # python_data = JSONParser().parse(streamed_data)

        python_data = common_lines(request)

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

from rest_framework.decorators import api_view

"""
@csrf_exempt
@api_view(["GET", "POST", "PUT", "DELETE"])
def student_api(request):
    if request.method == 'GET':    #-----require id
        # bytes_data = request.body
        # streamed_data = io.BytesIO(bytes_data)  #----json data
        # python_dict = JSONParser().parse(streamed_data)    #--dict

        python_dict = common_lines(request)

        sid = python_dict.get("id")   #---none
        if sid:
            #----for the single data
            try:
                stud = Student.objects.get(id=sid)
            except Student.DoesNotExist:
                msg = {"error" : "given id doesnot exit....!"}
                res = JSONRenderer().render(msg)
                return HttpResponse(res, content_type='application/json')
            ser = StudentSerializer(stud)         #-complex to native python-
            # json_data = JSONRenderer().render(ser.data)
            # return HttpResponse(json_data, content_type='application/json')

            #--single line
            return JsonResponse(ser.data)

        #----for the all data
        studs = Student.objects.all()
        ser = StudentSerializer(studs, many=True)
        # json_data = JSONRenderer().render(ser.data)
        # return HttpResponse(json_data, content_type='application/json')

        return JsonResponse(ser.data, safe=False)   #---to multiple data safe= False


            
    elif request.method == 'POST':   #----send user data
        # data1 = request.data  #-----python dict
        # bytes_data = request.body
        # streamed_data = io.BytesIO(bytes_data)  #----json data
        # python_dict = JSONParser().parse(streamed_data)

        python_dict = common_lines(request)

        print(python_dict)
        ser = StudentSerializer(data=python_dict)
        if ser.is_valid():
            ser.save()
            return JsonResponse({"msg" : "data insert successfully"})
        return JsonResponse({"error" : ser.errors})



    elif request.method == 'PUT':        #------id --along with data which is to be update
        # bytes_data = request.body
        # streamed_data = io.BytesIO(bytes_data)  #----json data
        # python_dict = JSONParser().parse(streamed_data)

        python_dict = common_lines(request)

        sid = python_dict.get("id")
        print(python_dict)  #---new data
        if sid:
            stud = Student.objects.get(id=sid)
        ser = StudentSerializer(instance=stud, data=python_dict, partial=True)

        if ser.is_valid():
            ser.save()
            return JsonResponse({"msg" : "data update successfully"})
        return JsonResponse({"error" : ser.errors})



    elif request.method == 'DELETE':    #----user - id
        # bytes_data = request.body
        # streamed_data = io.BytesIO(bytes_data)  #----json data
        # python_dict = JSONParser().parse(streamed_data)

        python_dict = common_lines(request)

        sid = python_dict.get("id")
        print(python_dict)  #---new data
        if sid:
            stud = Student.objects.get(id=sid)
            stud.delete()
            return JsonResponse({"msg" : "data delete successfully"})
    

    else:
        msg = {"error" : "invalid request mathod"}   #python dict
        res = JSONRenderer().render(msg)           #-----convert into json
        return HttpResponse(res, content_type='application/json')


"""


#--class base views

from django.views import View
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name="dispatch")
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
        python_dict = common_lines(request)

        sid = python_dict.get("id")   #---none
        if sid:
            #----for the single data
            try:
                stud = Student.objects.get(id=sid)
            except Student.DoesNotExist:
                msg = {"error" : "given id doesnot exit....!"}
                res = JSONRenderer().render(msg)
                return HttpResponse(res, content_type='application/json')
            ser = StudentSerializer(stud)         #-complex to native python-
            # json_data = JSONRenderer().render(ser.data)
            # return HttpResponse(json_data, content_type='application/json')

            #--single line
            return JsonResponse(ser.data)

        #----for the all data
        studs = Student.objects.all()
        ser = StudentSerializer(studs, many=True)
        # json_data = JSONRenderer().render(ser.data)
        # return HttpResponse(json_data, content_type='application/json')

        return JsonResponse(ser.data, safe=False)   #---to multiple data safe= False



    def post(self, request, *args, **kwargs):
        python_dict = common_lines(request)

        print(python_dict)
        ser = StudentSerializer(data=python_dict)
        if ser.is_valid():
            ser.save()
            return JsonResponse({"msg" : "data insert successfully"})
        return JsonResponse({"error" : ser.errors})


    def put(self, request, *args, **kwargs):
        python_dict = common_lines(request)

        sid = python_dict.get("id")
        print(python_dict)  #---new data
        if sid:
            stud = Student.objects.get(id=sid)
        ser = StudentSerializer(instance=stud, data=python_dict, partial=True)

        if ser.is_valid():
            ser.save()
            return JsonResponse({"msg" : "data update successfully"})
        return JsonResponse({"error" : ser.errors})


    def delete(self, request, *args, **kwargs):
        python_dict = common_lines(request)

        sid = python_dict.get("id")
        print(python_dict)  #---new data
        if sid:
            stud = Student.objects.get(id=sid)
            stud.delete()
            return JsonResponse({"msg" : "data delete successfully"})
    

@api_view(["GET", "POST", "PUT", "DELETE"])
def student_api(request):
    if request.method == "GET":
        pass

    if request.method == "POST":
        pass

    if request.method == "PUT":
        pass

    if request.method == "DELETE":
        pass



