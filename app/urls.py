from .views import *
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns=[
    # path('home/',home,name="home"),
    path('students/',get_students),
    path('cs/',create_student),
    path('ss/',serialize_student),
    path('demo/',demo),
    path('obtain_auth/',obtain_auth_token),
    path('logout/',logout_view),
    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view()),
    path('demo_jwt/',demo_jwt),
    path('custom_jwt/',custom_jwt),

    path('student_list/',student_list),
    path('StudentList/',StudentList.as_view()),
    path('create_student/',CreateStudent.as_view()),
    path('update_student/<int:pk>/',UpdateStudent.as_view()),
    path('retrieve_student/<int:pk>/',RetrieveStudent.as_view()),
    path('destroy_student/<int:pk>/',DestroyStudent.as_view())

]