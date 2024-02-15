from django.db import models

# Create your models here.

class Student(models.Model):
    stname = models.CharField( max_length=50)
    stemail = models.EmailField( max_length=254)