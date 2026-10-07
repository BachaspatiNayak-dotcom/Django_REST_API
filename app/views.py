from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import *
from .serializers import *

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
@authentication_classes([TokenAuthentication]) #who is this mf
@permission_classes([IsAuthenticated]) #what is he allowed to do
def demo(request):
    return Response("this is demo page")