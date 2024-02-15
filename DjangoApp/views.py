from django.shortcuts import render
from .models import *
from .serializers import StudentSerializer , addStudent
from rest_framework.generics import ListAPIView , CreateAPIView
from rest_framework import generics,status
from rest_framework.response import Response


import os 
from django.conf import settings
from django.http import HttpResponse
# Create your views here.


def index(request):
    path = os.path.join(settings.BASE_DIR, "reactfrontend", "build", "index.html")
    with open(path, 'r') as file:
        html_content = file.read()

    return HttpResponse(html_content)


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class addStudent(CreateAPIView):
    serializer_class = addStudent

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            student = Student(stname=serializer.data.get('stname'), stemail=serializer.data.get('stemail'))
            student.save()
            return Response({'status': 'success'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'error', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
