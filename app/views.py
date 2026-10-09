from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView,RetrieveAPIView
from django.contrib.auth import authenticate
from .models import *
from .serializers import *
from .tokens import *
from .pagination import *

# Create your views here.

# def home(request):
#     data=[
#         {"id":101,"name":"Sachin"},
#         {"id":102,"name":"Anandita"}
#     ]

#     return JsonResponse(data,safe=False)


# @api_view(['GET'])
# def students(request):
#     data = [
#         {"id": 1, "name": "Sachin"},
#         {"id": 2, "name": "Rahul"}
#     ]

#     return Response(data)

@api_view(['GET'])
def get_students(request):
    data=Student.objects.all()
    serializer=StudentSerializer(data,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_student(request):
    name=request.data.get("name")
    age=request.data.get("age")
    email=request.data.get("email")
    adress=request.data.get("adress")

    Student.objects.create(name=name,age=age,email=email,adress=adress)

    return Response({"status":200,"msg":"student craeted successfully"})
    
@api_view(['POST'])
def serialize_student(request):

    serialize=StudentSerializer(data=request.data)

    if serialize.is_valid():
        serialize.save()
        return Response({"msg":"all fields are valid,student object created successfully"})

    return Response(serialize.errors)


@api_view(['POST'])
@authentication_classes([JWTAuthentication]) #who is this mf
@permission_classes([IsAuthenticated]) #what is he allowed to do #similar to @login_required
def demo(request):
    return Response("this is demo page")


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout_view(request):
    request.auth.delete()
    return Response({"status":200,"msg":"you got logged out successfully"})


@api_view(['POST'])
@authentication_classes([JWTAuthentication]) #who is this mf #this is optional in JWT
@permission_classes([IsAuthenticated]) #what is he allowed to do #similar to @login_required
def demo_jwt(request):
    return Response("this is demo page using jwt")


@api_view(['POST'])
def custom_jwt(request):
    un=request.data.get("username")
    pw=request.data.get("password")

    user=authenticate(username=un,password=pw)

    if user:
        custom_token=MyToken.for_user(user)

        return Response({
            'message':'Login successful....',
            'refresh':str(custom_token),
            'access':str(custom_token.access_token)
        })

    return Response({'msg':'no user is found'})




@api_view(['GET'])
def student_list(request):
    students=Student.objects.all()

    paginator=MyPagination()

    page=paginator.paginate_queryset(
        students,
        request
    )

    serialize=StudentSerializer(page,many=True)

    # return Response(serialize.data)  -->sends the raw data

    return paginator.get_paginated_response(
        serialize.data
    )  #sends the meta data




class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    # pagination_class=MyPagination


class CreateStudent(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class UpdateStudent(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class DestroyStudent(DestroyAPIView):
    queryset=Student.objects.all()
    # serializer_class=StudentSerializer

class RetrieveStudent(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer



