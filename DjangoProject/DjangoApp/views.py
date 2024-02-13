from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import *
import os 
from django.conf import settings
from django.http import HttpResponse

# Create your views here.


def index(request):
    path = os.path.join(settings.BASE_DIR, "reactfrontend", "build", "index.html")
    print("Path is: ", path)

    with open(path, 'r') as file:
        html_content = file.read()

    return HttpResponse(html_content)


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
