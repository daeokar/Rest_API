from django.shortcuts import render
from first_app.models import Student, Collge
from first_app.serializers import StudentSerializer, CollegeSerializer
from rest_framework.renderers import JSONRenderer  # python to json
from rest_framework.parsers import JSONParser  # json to python
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


# CRUD -- 
def single_stud(request, pk):
    print("In single stud API", '######') #
    stud_obj = Student.objects.get(id=pk)   # complex data type
    python_obj = StudentSerializer(stud_obj)   # complex data type to native python data type
    json_data = JSONRenderer().render(python_obj.data)  # python to json
    return HttpResponse(json_data, content_type='application/json')

def all_stud(request):
    print("In all stud API", '######')
    studs = Student.objects.all()
    python_obj = StudentSerializer(studs, many=True)
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
        # print(python_data)     #    {'name': 'CCC', 'age': 19, 'city': 'Nanded', 'marks': 65}
        ser = StudentSerializer(data=python_data)
        print(ser)
        if ser.is_valid():
            ser.save()   # calls create() method of StudentSerialiazer
            msg = {"msg": "data created successfully...!"}
            res = JSONRenderer().render(msg)
        return HttpResponse(res, content_type='application/json')
    else:
        msg = {"error": "only post method allowed"}
        res = JSONRenderer().render(msg)
        return HttpResponse(res, content_type='application/json') # 

from rest_framework.decorators import api_view

def common_lines(request):
    bytes_data = request.body
    streamed_data = io.BytesIO(bytes_data)  # json data
    python_dict = JSONParser().parse(streamed_data) 
    return python_dict


# 26 june -- 2 video -- blogs -- 

"""
@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_api(request):
    if request.method == 'GET':   # id pass -- single data, id {} - all data, 
        # bytes_data = request.body
        # streamed_data = io.BytesIO(bytes_data)  # json data
        # python_dict = JSONParser().parse(streamed_data)   # dict  ---   {} or {"id": 1}

        python_dict = common_lines(request)

        sid = python_dict.get("id")  # None
        print(python_dict)
        if sid:
            # for single data
            try:
                stud = Student.objects.get(id=sid)
            except Student.DoesNotExist:
                msg = {"error": "given id does not exist..!"}
                res = JSONRenderer().render(msg)
                return HttpResponse(res, content_type='application/json') #
            ser = StudentSerializer(stud)   # complex to native python
            # json_data = JSONRenderer().render(ser.data)
            # return HttpResponse(json_data, content_type='application/json')

            # single line
            return JsonResponse(ser.data)

        # for all data
        studs = Student.objects.all()
        ser = StudentSerializer(studs, many=True)
        # json_data = JSONRenderer().render(ser.data)
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(ser.data, safe=False)

    elif request.method == 'POST':   # user data send
        # data1 = request.data # python dict  # {"name": "EEE", "age": 21, "city": "Panvel", "marks": 75}
        # bytes_data = request.body
        # streamed_data = io.BytesIO(bytes_data)  # json data
        # python_dict = JSONParser().parse(streamed_data)
        
        python_dict = common_lines(request)
        
        # print(python_dict)
        ser = StudentSerializer(data=python_dict)
        if ser.is_valid():
            ser.save()
            return JsonResponse({"msg": "data inserted successfully..!"})
        return JsonResponse({"error": ser.errors})
    elif request.method == 'PUT':  # id--along with data which is to be updated
        # bytes_data = request.body
        # streamed_data = io.BytesIO(bytes_data)  # json data
        # python_dict = JSONParser().parse(streamed_data)

        python_dict = common_lines(request)

        sid = python_dict.get("id")  # None
        print(python_dict)  # new_data
        if sid:
        # print(python_dict)
            stud = Student.objects.get(id=sid)  # existing data fetched from database

        ser = StudentSerializer(instance=stud, data=python_dict, partial=True)
        if ser.is_valid():
            ser.save()
            return JsonResponse({"msg": "data updated successfully..!"})
        return JsonResponse({"error": ser.errors})
    
    elif request.method == 'DELETE':  # user - id
        # bytes_data = request.body
        # streamed_data = io.BytesIO(bytes_data)  # json data
        # python_dict = JSONParser().parse(streamed_data)

        python_dict = common_lines(request)

        sid = python_dict.get("id")  # None
        print(python_dict)  # new_data
        if sid:
            stud = Student.objects.get(id=sid)
            stud.delete()
            return JsonResponse({"msg": "data deleted successfully..!"})
    else:
        msg = {"error": "invalid request method"}  # python dict
        res = JSONRenderer().render(msg)  # json madhe convert
        return HttpResponse(res, content_type='application/json')

"""
# class based view



from django.views import View
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
        python_dict = common_lines(request)

        sid = python_dict.get("id")  # None
        print(python_dict)
        if sid:
            # for single data
            try:
                stud = Student.objects.get(id=sid)
            except Student.DoesNotExist:
                msg = {"error": "given id does not exist..!"}
                res = JSONRenderer().render(msg)
                return HttpResponse(res, content_type='application/json') #
            ser = StudentSerializer(stud)   # complex to native python
            # json_data = JSONRenderer().render(ser.data)
            # return HttpResponse(json_data, content_type='application/json')

            # single line
            return JsonResponse(ser.data)

        # for all data
        studs = Student.objects.all()
        ser = StudentSerializer(studs, many=True)
        # json_data = JSONRenderer().render(ser.data)
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(ser.data, safe=False)


    def post(self, request, *args, **kwargs):
           
        python_dict = common_lines(request)
        
        # print(python_dict)
        ser = StudentSerializer(data=python_dict)
        if ser.is_valid():
            ser.save()
            return JsonResponse({"msg": "data inserted successfully..!"})
        return JsonResponse({"error": ser.errors})

    def put(self, request, *args, **kwargs):
        python_dict = common_lines(request)

        sid = python_dict.get("id")  # None
        print(python_dict)  # new_data
        if sid:
        # print(python_dict)
            stud = Student.objects.get(id=sid)  # existing data fetched from database

        ser = StudentSerializer(instance=stud, data=python_dict, partial=True)
        if ser.is_valid():
            ser.save()
            return JsonResponse({"msg": "data updated successfully..!"})
        return JsonResponse({"error": ser.errors})

    def delete(self, request, *args, **kwargs):
        python_dict = common_lines(request)

        sid = python_dict.get("id")  # None
        print(python_dict)  # new_data
        if sid:
            stud = Student.objects.get(id=sid)
            stud.delete()
            return JsonResponse({"msg": "data deleted successfully..!"})

    

# api_view -- 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# browsable APIs -- 

@api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])  # by default - GET
def student_api(request, pk=None):  #  25
    if request.method == 'GET':
        sid = pk # request.data.get('id')  # None
        if sid:
            stud = Student.objects.get(id=sid)
            ser = StudentSerializer(stud)
            return Response(ser.data)
        else:
            studs = Student.objects.all()
            ser = StudentSerializer(studs, many=True)
            return Response(ser.data)
            
    elif request.method == 'POST':
        print(request.data)  # parse - python dict
        data1 = request.data
        ser = StudentSerializer(data=data1)
        if ser.is_valid():
            ser.save()
            return Response({"msg": "Data Created", "data": request.data}, status=status.HTTP_201_CREATED)  #  200
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        stud = Student.objects.get(id=pk)   # request.data.get('id')
        ser = StudentSerializer(instance=stud, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg": "Complete Data updated for id {}".format(pk)})
        return Response(ser.errors)

    elif request.method == 'PATCH':
        stud = Student.objects.get(id=pk)
        ser = StudentSerializer(instance=stud, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response({"msg": "Partial Data updated for id {}".format(pk)})
        return Response(ser.errors)

    elif request.method == 'DELETE':
        pass
    
##############################
# - @api_view
# APIView  class  - sublcass of View  ---

from rest_framework.views import APIView

class StudentAPINew(APIView):
    def get(self, request, pk=None, format=None):
        sid = pk
        if sid:
            stud = Student.objects.get(id=sid)
            ser = StudentSerializer(stud)
            return Response(ser.data)

        studs = Student.objects.all()
        ser =  StudentSerializer(studs, many=True)
        return Response(ser.data)

    def post(self, request, format=None):
        data = request.data  # python dict
        ser = StudentSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response({"msg": "data created..", "data": request.data}, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)        

    def put(self,pk, request, format=None):
        sid = pk
        if sid:
            stud = Student.objects.get(id=sid)
            ser = StudentSerializer(instance=stud, data=request.data)
            if ser.is_valid():
                ser.save()
                return Response({"msg": "complete data updated..", "data": ser.data}, status=status.HTTP_200_OK)
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)        


    def patch(self, pk,request, format=None):
        sid = pk
        if sid:
            stud = Student.objects.get(id=sid)
            ser = StudentSerializer(instance=stud, data=request.data, partial=True)
            if ser.is_valid():
                ser.save()
                return Response({"msg": "partial data updated..", "data": ser.data}, status=status.HTTP_200_OK)
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)        

    def delete(self, pk, request, format=None):  # try 
        pass  #softdelete    is_deleted = 0
        # studs = Student.objects.filter(is_deleted=0)


# GenericAPIView   -- subclass of APIView
# already defined common beheviours  -- 

# - queryset -- Student.objects.all()
# - serializer_class -- StudentSerializer

# Mixins:-
# ListModelMixin -- all data
# RetrieveModelMixin  - single data
# CreateModelMixin  -- for post request, 
# UpdateModelMixin -- update
# DestroyModelMixin  -- delete

from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView

class StudList(GenericAPIView, ListModelMixin):
    queryset = Student.objects.all()  # GenericAPIView
    serializer_class = StudentSerializer  # GenericAPIView

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)  # ListModelMixin

class StudCreate(GenericAPIView, CreateModelMixin):
    queryset = Student.objects.all()  # GenericAPIView
    serializer_class = StudentSerializer  # GenericAPIView

    def post(self, request,  *args, **kwargs):
        return self.create(request, *args, **kwargs)


# classes which requird pk/id

class StudRetrieve(GenericAPIView, RetrieveModelMixin):
    queryset = Student.objects.all()  # GenericAPIView
    serializer_class = StudentSerializer  # GenericAPIView
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(self, request, *args, **kwargs)

class StudUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Student.objects.all()  # GenericAPIView
    serializer_class = StudentSerializer  # GenericAPIView

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class StudDestroy(GenericAPIView, DestroyModelMixin):
    queryset = Student.objects.all()  # GenericAPIView
    serializer_class = StudentSerializer  # GenericAPIView

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# combined mixins -- 

class StudListCreate(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()  # GenericAPIView
    serializer_class = StudentSerializer  # GenericAPIView

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)  # L

    def post(self, request,  *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudRetrieveUpdateDestroy(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()  # GenericAPIView
    serializer_class = StudentSerializer  # GenericAPIView

    def get(self, request, *args, **kwargs):
        return self.retrieve(self, request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# Concrete Generic API View Classes

from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView 


class StudListC(ListAPIView):   # inherit GenericAPIView, ListModelMixin
    queryset = Student.objects.all() 
    serializer_class = StudentSerializer 

class StudCreateC(CreateAPIView):
    queryset = Student.objects.all() 
    serializer_class = StudentSerializer 

class StudRetrC(RetrieveAPIView):
    queryset = Student.objects.all() 
    serializer_class = StudentSerializer 

class StudUpdC(UpdateAPIView):
    queryset = Student.objects.all() 
    serializer_class = StudentSerializer 

class StudDestrC(DestroyAPIView):
    queryset = Student.objects.all() 
    serializer_class = StudentSerializer 




#########  Viewsets ---
# - repeated logic can be combined in one code base
# - url routers --- to generate urls automatically, u dont need to define urls explicitely
# no handler methods -- get(), post(), put(), patch(), delete()
# - provides - list(), retrieve(), update(), partial_update(),destroy(), create()

from rest_framework.viewsets import ViewSet

class StudentViewSet(ViewSet):
    def list(self, request):
        studs = Student.objects.all()
        ser = StudentSerializer(studs, many=True)
        return Response(ser.data)

    def create(self, request):
        ser = StudentSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        sid = pk
        if sid:
            stud = Student.objects.get(id=sid)
            ser = StudentSerializer(stud)
            return Response(ser.data)
    
    def update(self, request, pk):
        sid = pk
        if sid:
            stud = Student.objects.get(id=sid)
            ser = StudentSerializer(instance=stud, data=request.data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data, status=status.HTTP_200_OK)
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        sid = pk
        if sid:
            stud = Student.objects.get(id=sid)
            ser = StudentSerializer(instance=stud, data=request.data, partial=True)
            if ser.is_valid():
                ser.save()
                return Response(ser.data, status=status.HTTP_200_OK)
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        pass  # status 204

    

#ModelViewSet 

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet  # -- read
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

# AllowAny   -- get all permission irrespective if user authentication
# IsAuthenticated  -- permits to only authenticated user -- no matter which user ur using -- in point of is_
# IsAdminUser -- user which has is_staff enabled, only that user has all access

from rest_framework.decorators import action


class StudentModelViewSet(ModelViewSet):  # CRUD
    # queryset = Student.objects.all().filter(is_deleted=0)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [AllowAny]  # by default -- permission -- AlloWAny
    # permission_classes = [IsAuthenticated] 
    # permission_classes = [IsAdminUser]  \
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly] 
    # lookup_field = 'name'
    # lookup_url_kwarg
    # lookup_value_regex 

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]  # by default -- permission -- AlloWAny

"""
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).filter(is_deleted=0)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):  # overridden method -- from mixins -DestroMixin
        instance = self.get_object()
        instance.is_deleted = 1
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
     


     # new url defined   # @list_route  -- substitute
    @action(methods=['get'], detail=False, url_path='get-deleted-data', url_name='get-deleted-data')
    def get_deleted_records(self, request):
        queryset = self.filter_queryset(self.get_queryset()).filter(is_deleted=1)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
"""
class CollegeModelViewSet(ModelViewSet):
    queryset = Collge.objects.all()
    serializer_class = CollegeSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [AllowAny] 

    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated] 
     


# testing

# - postman
# - request_client.py
# - api roots - drf
# - curl
# - httpie

# - django rest swagger  --- testing, api documentation

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


from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


# Filtering

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

class StudPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 5
    # page_query_param = 'p'




class StudListF(ListAPIView):   # inherit GenericAPIView, ListModelMixin
    queryset = Student.objects.all() 
    serializer_class = StudentSerializer 
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['id', 'name', 'marks']   # http://127.0.0.1:8000/stud-filter/?name=Raju&marks=75
    pagination_class = StudPagination

    # filter_backends = [SearchFilter]
    search_fields = ['=id', 'name']

    # authentication_classes = (BasicAuthentication,)
    # permission_classes = (IsAuthenticated,)

    # def get_queryset(self):
    #     return Student.objects.filter(city='Pune')

    # def get_queryset(self):
        # """
        # This view should return a list of all the students
        # for the currently authenticated user.
        # """
        # user = self.request.user  # object
        # print(user)
        # return Student.objects.filter(created_by=user)

        # queryset = Student.objects.all()
        # username = self.request.query_params.get('username')
        # if username is not None:
        #     queryset = queryset.filter(created_by__username=username)
        # return queryset
    

from first_app.serializers import AlbumSerializer, TrackSerializer
from first_app.models import Album, Track
from rest_framework.viewsets import ModelViewSet


class AlbumModelViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class TrackModelViewSet(ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


