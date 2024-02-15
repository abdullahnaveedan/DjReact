from django.shortcuts import render
from django.conf import settings
import os
from django.http import HttpResponse


def q(request):
    path = os.path.join(settings.BASE_DIR, "reactfrontend", "build", "index.html")
    print("Path is: ", path)
    with open(path, 'r') as file:
        html_content = file.read()
    return HttpResponse(html_content)