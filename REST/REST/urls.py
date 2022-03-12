"""REST URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from first_app.views import *
from first_app.urls import router
from django.conf.urls import url


from rest_framework.authtoken.views import obtain_auth_token
from first_app.views import login_token
from rest_framework_simplejwt import views as jwt_views


from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Student Operation API')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('get-stud/<int:pk>/', single_stud),
    # path('get-all-stud/', all_stud),
    # path('create-data/', create_data),

    # single api for all methods
    # path('student-api/', student_api),
    
    # class based view
    # path("stud-class-api/", StudentAPI.as_view()),

    # path("studentapi/", student_api),
    # path("studentapi/<int:pk>/", student_api),

    # APIView class
    # path("studentapinew/", StudentAPINew.as_view()),   # post, get-- all data
    # path("studentapinew/<int:pk>/", StudentAPINew.as_view()),   # get -single data, put, patch, delete

    # Mixins and GenericAPIView
    # path("s-list/", StudList.as_view()), 
    # path("s-create/", StudCreate.as_view()), 
    # path("s-retrieve/<int:pk>/", StudRetrieve.as_view()), 
    # path("s-update/<int:pk>/", StudUpdate.as_view()), 
    # path("s-destroy/<int:pk>/", StudDestroy.as_view()), 


    # combined mixins
    # path("s-list-create/", StudListCreate.as_view()), 
    # path("s-retrieve-update-destroy/<int:pk>/", StudRetrieveUpdateDestroy.as_view()), 


    # concrete API View class
    # path("s-list-c/", StudListC.as_view()), 
    # path("s-create-c/", StudCreateC.as_view()), 
    # path("s-update-c/<int:pk>/", StudUpdC.as_view()), 
    # path("s-retr-c/<int:pk>/", StudRetrC.as_view()), 
    # path("s-destr-c/<int:pk>/", StudDestrC.as_view()), 

    # combine concrete classes

    # ViewSet
    path('', include(router.urls)),
    # url(r'^$', schema_view),
    # url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),  # login url, logout url

    # path('api-token/', obtain_auth_token, name='api_token_auth'),
    # path('login-token/', login_token, name='api_token_auth1'),

    # JWT
    # path('hello/', HelloView.as_view(), name='hello'),

    # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    # path('stud-filter/', StudListF.as_view()),
    
]
