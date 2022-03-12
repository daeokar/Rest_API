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
from django.urls import path
from rest_app.views import * 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('single_stud/<int:pk>/', single_stud),
    path('all_stud/', all_stud),
    path('create_data/', create_data),

    #----single api for all method

    # path('student_api/', student_api),

    #---class base view

    path('stud_class_api/', StudentAPI.as_view()),

    #---api url

    path('student_api/', student_api),
    path('student_api/<int:pk>/', student_api),

]
