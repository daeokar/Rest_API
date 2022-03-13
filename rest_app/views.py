from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from rest_app.models import *
from rest_app.serilizers import *

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

from django.utils.decorators import method_decorator
from django.views import View


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


#-########################################################################
    

from rest_framework.response import Response

"""
@api_view(["GET", "POST", "PUT", "DELETE", "PATCH"])   #----by default GET
def student_api(request):
    if request.method == "GET":
        sid = request.data.get("id")
        if sid:
            stud = Student.objects.get(id=sid)
            ser = StudentSerializer(stud)
            return Response(ser.data)
        else:
            studs = Student.objects.all()
            ser = StudentSerializer(studs, many=True)
            return Response(ser.data)

    if request.method == "POST":
        data1 = request.data
        ser = StudentSerializer(data=data1)
        if ser.is_valid():
            ser.save()
            return Response({"msg" : "Data created successfully"})
        else:
            return Response(ser.errors)

    if request.method == "PUT":
        sid = request.data.get("id")
        stud = Student.objects.get(id=sid)
        ser = StudentSerializer(instance=stud, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg" : "Data update for {}".format(request.data.get("id"))})
        else:
            return Response(ser.errors)

    if request.method == "PATCH":
        sid = request.data.get("id")
        stud = Student.objects.get(id=sid)
        ser = StudentSerializer(instance=stud, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response({"msg" : "Data update for {}".format(request.data.get("id"))})
        else:
            return Response(ser.errors)

    if request.method == "DELETE":
        sid = request.data.get("id")
        stud = Student.objects.get(id=sid)
        stud.delete()
        return Response({"msg" : {"data delete successfully...!"}})

"""
#-------#########################################################################

#---Browsable API---

from rest_framework import status


@api_view(["GET", "POST", "PUT", "DELETE", "PATCH"])   #----by default GET
def student_api(request, pk):
    if request.method == "GET":
        sid = request.data.get("id")
        if sid:
            stud = Student.objects.get(id=sid)
            ser = StudentSerializer(stud)
            return Response(ser.data) 
        else:
            studs = Student.objects.all()
            ser = StudentSerializer(studs, many=True)
            return Response(ser.data)

    if request.method == "POST":
        data1 = request.data
        ser = StudentSerializer(data=data1)
        if ser.is_valid():
            ser.save()
            return Response({"msg" : "Data created successfully", "data" : request.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors)

    if request.method == "PUT":
        sid = request.data.get("id")
        stud = Student.objects.get(id=sid)
        ser = StudentSerializer(instance=stud, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg" : "complete Data update for {}".format(pk)})
        else:
            return Response(ser.errors)

    if request.method == "PATCH":
        sid = request.data.get("id")
        stud = Student.objects.get(id=sid)
        ser = StudentSerializer(instance=stud, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response({"msg" : "Partial Data update for {}".format(pk)})
        else:
            return Response(ser.errors)

    if request.method == "DELETE":
        sid = request.data.get("id")
        stud = Student.objects.get(id=sid)
        stud.delete()
        return Response({"msg" : {"data delete successfully...!"}})


#################################################################################################
# --apiviews

#-----APIView class -----is sub class of View

from rest_framework.views import APIView


class StudentAPIViews(APIView):
    def get(self, request, pk=None, format=None ):
        sid = pk
        if sid:
            stud = Student.objects.get(id=sid)
            ser = StudentSerializer(stud)
            return Response(ser.data)
        
        studs = Student.objects.all()
        ser = StudentSerializer(studs, many=True)
        return Response(ser.data)

    def post(self, request, format=None):
        data = request.data                                                #python dict ---Unserialize data
        ser = StudentSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response({"msg" : "Data Created Successfully....!", "data" : ser.data}, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        sid = pk
        if sid:
            stud = Student.objects.get(id=sid)
            ser = StudentSerializer(instance=stud, data=request.data)
            if ser.is_valid():
                ser.save()
                return Response({"msg" : "complete data updated....!", "data" : ser.data}, status=status.HTTP_201_CREATED)
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None, format=None):
        sid = pk
        if sid:
            stud = Student.objects.get(id=sid)
            ser = StudentSerializer(instance=stud, data=request.data, partial=True)
            if ser.is_valid():
                ser.save()
                return Response({"msg" : "partialy data updated....!", "data" : ser.data}, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk=None, format=None):
        sid = pk
        if sid:
            stud = Student.objects.get(id=sid)
            stud.delete()
            return Response({"msg" : "Data deleted  Successfully....!"})

#################################################################################################################


#---------------------------By using generic api views----------- Mixins----------

#--GenericAPIView   -- subclass of APIView

#--- already defined common beheviours  -- 

# - queryset -- Student.objects.all()
# - serializer_class -- StudentSerializer

# Mixins:-
# ListModelMixin -- all data
# RetrieveModelMixin  - single data
# CreateModelMixin  -- for post request, 
# UpdateModelMixin -- update
# DestroyModelMixin  -- delete

from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView

class StudentList(GenericAPIView, ListModelMixin):
    queryset = Student.objects.all()                                  #----GenericAPIView
    serializer_class = StudentSerializer                              #----GenericAPIView

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)                    #-----ListModelMixin

class StudentCreate(GenericAPIView, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)                  #----CreateModelMixin

#------ Required id -----

class StudentRetrive(GenericAPIView, RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)                 #----RetrieveModelMixin

class StudentUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)                    #-----UpdateModelMixin

    

class StudentDestroy(GenericAPIView, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)                    #------DestroyModelMixin

    
##################################################################################################    


#-----Common mixing-----

class StudListCreate(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):                               #----to get all data ------get
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):                              #----to create data   -----post
        return self.create(request, *args, **kwargs)

 

class StudRetriveUpdateDestroy(GenericAPIView, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):                                #---to get the single data  -----get
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):                                #----to update the data ----- put, patch
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):                             #----to delete data  -------delete
        return self.destroy(request, *args, **kwargs)


################################################################################################

from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView


class StudentListC(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCreateC(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetriveC(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdateC(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDestroyC(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


#####################################################################################################





