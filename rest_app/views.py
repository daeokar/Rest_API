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

#----Concreat APIViews---

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

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class StudListCreateView(ListCreateAPIView):                                               #---combine the two views -- list, create in single class 
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):                          #---combine the three views --retrive , update, destroy, in single class 
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


#######################################################################################################


#----  Viewsets ---
# - repeated logic can be combined in one code base
# - url routers --- to generate urls automatically, u dont need to define urls explicitely
# no handler methods -- get(), post(), put(), patch(), delete()
# - provides - list(), retrieve(), update(), partial_update(),destroy(), create()

from rest_framework.viewsets import ViewSet

class StudentViewset(ViewSet):
    def list(self, request):
        studs = Student.objects.all()
        ser = StudentSerializer(studs, many=True)
        return Response(ser.data)

    def create(self, request):
        data = request.data
        ser = StudentSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk):
        sid = pk
        if sid:
            stud = Student.objects.get(id=sid)
            ser = StudentSerializer(stud)
            return Response(ser.data, status=status.HTTP_200_OK)

    def update(self, request, pk):
        sid = pk 
        if sid:
            stud = Student.objects.get(id=sid)
            ser = StudentSerializer(instance=stud, data=request.data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data, status=status.HTTP_201_CREATED)
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


    def partial_update(self, request, pk):
        sid = pk 
        if sid:
            stud = Student.objects.get(id=sid)
            ser = StudentSerializer(instance=stud, data=request.data, partial=True)
            if ser.is_valid():
                ser.save()
                return Response(ser.data, status=status.HTTP_201_CREATED)
            return Response(ser.data, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        sid = pk
        if sid:
            stud = Student.objects.get(id=sid)
            stud.delete()
            return Response({"msg" : "Data deleted successfully....!"}, status=status.HTTP_204_NO_CONTENT)

#################################################################################################################

from rest_framework.viewsets import ModelViewSet , ReadOnlyModelViewSet
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.decorators import action

# AllowAny   -- get all permission irrespective if user authentication
# IsAuthenticated  -- permits to only authenticated user -- no matter which user ur using -- in point of is_
# IsAdminUser -- user which has is_staff enabled, only that user has all access


class StudentModelViewset(ModelViewSet):
    # queryset = Student.objects.all().filter(is_deleted=0)    #---fetach on li active data 
    queryset = Student.objects.all()                         #-----to fetach all data
    serializer_class = StudentSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [AllowAny]         #----------by default -- permission -- AlloWAny
    # permission_classes = [IsAuthenticated] 
    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticatedOrReadOnly]   #-----only read the data
    # lookup_field = "name"
    # lookup_url_kwarg =

    #-----tokan athontication ---

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


"""
    #----ovearriding----- 

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).filter(is_deleted=0)      #-----queryset = Student.objects.all().filter(is_deleted=0)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):         #--over riden method
        instance = self.get_object()
        # print(instance)
        instance.is_deleted = 1
        instance.save() 
        return Response(status=status.HTTP_204_NO_CONTENT)

    # ---- new url defined   #----   @list_route --substittude (also use to generete the url ..)
    @action(methods=['get'], detail=False, url_path='get-deleted-data', url_name='get-deleted-data')            #----queryset = Student.objects.all().filter(is_deleted=1)
    def get_deleted_records(self, request):

        queryset = self.filter_queryset(self.get_queryset()).filter(is_deleted=1)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

"""


#-----by using the  ReadOnlyModelViewSet

class StudentReadOnlyModelViewset(ReadOnlyModelViewSet):     #-----we ca only read the data
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



class CollageModelViewset(ModelViewSet):
    queryset = Collage.objects.all()
    serializer_class = CollageSerializar
    # authentication_classes = [SessionAuthentication]
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login_token(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key, "email":user.email, "first_name": user.first_name},status=HTTP_200_OK)



# testing

# - postman
# - request_client.py
# - api roots - drf
# - curl
# - httpie

# - django rest swagger  --- testing, api documentation


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

############################################################################################################################

#-----filtering 
#----search filter --

from django_filters.rest_framework import DjangoFilterBackend                    #------it is support the high customizable fileds filtering for rest fream work
from rest_framework.filters import SearchFilter                                  #-----only appplide if the view has a search_fields

class StudentListFilter(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = (BasicAuthentication,)                            #----to authenticated person log in
    # permission_classes = (IsAuthenticated,)                            
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['id', 'name']
    search_fields = ['name', 'id']


    # def get_queryset(self):
        # return Student.objects.filter(city="arvi")                              #----to filter the data and get

        # user = self.request.user              #----the user which login
        # # return Student.objects.filter(created_by__username=user)
        # return Student.objects.filter(created_by=user)

        # queryset = Student.objects.all()
        # username = self.request.query_params.get("username")                       #-----?username=name of user
        # if username is not None:
        #     queryset = queryset.filter(created_by__username=username)
        # return queryset


#------  Ordering Filter -------

from rest_framework.filters import OrderingFilter                                 #-----only appplide if the view has a ordering_fields


class StudListOrderingFilter(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [OrderingFilter]                                            #-------http://127.0.0.1:8000/stud_order_filter/?ordering=name
    # ordering_fields = ["name", "email"]                                          #------ required for the Orderongfilter
    # ordering_fields = '__all__'                                                    #----to all the fields in the model
    # ordering = ['name']











