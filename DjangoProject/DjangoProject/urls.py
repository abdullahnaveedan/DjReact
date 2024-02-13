from django.contrib import admin
from django.urls import path , include
from . import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("app/", include("DjangoApp.urls")),
    path("", include("DjangoApp.urls")),
    # path("", views.index, name="index"),
]
