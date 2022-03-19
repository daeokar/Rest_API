"""REST URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from rest_app.urls import *
from rest_app.views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_swagger.views import get_swagger_view
from rest_app.views import login_token
from rest_framework_simplejwt import views as jwt_views

schema_view = get_swagger_view(title='Student Operation API')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('single_stud/<int:pk>/', single_stud),
    # path('all_stud/', all_stud),
    # path('create_data/', create_data),

    #----single api for all method
    # path('student_api/', student_api),

    #---class base view
    # path('stud_class_api/', StudentAPI.as_view()),

    #---api url
    # path('student_api/', student_api),
    # path('student_api/<int:pk>/', student_api),

    #---APIViews url
    # path('studentAPIViews/', StudentAPIViews.as_view()),
    # path('studentAPIViews/<int:pk>/', StudentAPIViews.as_view()),

    #---GenericAPIView  url ---
    # path('student_List/', StudentList.as_view()),
    # path('student_Create/', StudentCreate.as_view()),
    # path('student_Retrive/<int:pk>/', StudentRetrive.as_view()),
    # path('student_Update/<int:pk>/', StudentUpdate.as_view()),
    # path('student_Destroy/<int:pk>/', StudentDestroy.as_view()),


    #----common mixin
    # path('student_list_create/', StudListCreate.as_view()),
    # path('student_retrive_update_destroy/<int:pk>/', StudRetriveUpdateDestroy.as_view()),

    # ---concreate APIVews----
    # path('student_list_c/', StudentListC.as_view()),
    # path('student_create_c/', StudentCreateC.as_view()),
    # path('student_Retrive_c/<int:pk>/', StudentRetriveC.as_view()),
    # path('student_update_c/<int:pk>/', StudentUpdateC.as_view()),
    # path('student_destroy_c/<int:pk>/', StudentDestroyC.as_view()),

    #----combine concreate classes----
    # path('student_list_create_c/', StudListCreateView.as_view()),
    # path('student_retrive_update_destry_c/<int:pk>/', StudRetrieveUpdateDestroyView.as_view()),

    #---ViewSet---
    path('', include(router.urls)),
    # re_path(r'^$', schema_view),
    # re_path(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),  # login url, logout url

    #---tokens---
    # path('api-token/', obtain_auth_token, name='api_token_auth'),
    # path('login-token/', login_token, name='api_token_auth1'),

    #---json web token---
    # path('hello/', HelloView.as_view(), name='hello'),
    # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    #----stud filter---- search_filter
    # path('stud_filter/', StudentListFilter.as_view()),

    #----Ordering Filter ----
    # path('stud_order_filter/', StudListOrderingFilter.as_view()),

    #--- Paginations url ---
    path('stud_list_paginations/', StudlistPaginationRecord.as_view()),


]
