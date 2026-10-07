from .models import *
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Student
        fields='__all__'
        # fields=['name','age']
        # exclude=['age']
    
    def validate_name(self,value):
        for ch in value:
            if ch.isdigit():
                raise ValidationError("your name should not contain any digit")
        return value

    def validate_age(self,value):
        if value<18:
            raise ValidationError("age should be greater than 18")
        return value
