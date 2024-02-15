from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("students/", views.StudentList.as_view(), name="students"),
    path("addStudent/", views.addStudent.as_view(), name="addsts")
]
