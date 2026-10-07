from .views import *
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    # path('home/',home,name="home"),
    path('students/',get_students),
    path('cs/',create_student),
    path('ss/',serialize_student),
    path('demo/',demo),
    path('obtain_auth/',obtain_auth_token)
]