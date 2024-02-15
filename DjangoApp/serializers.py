from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'stname' , 'stemail']

class addStudent(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['stname' , 'stemail']
        