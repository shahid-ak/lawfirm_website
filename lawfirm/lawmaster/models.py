from django.db import models

# Create your models here.

class Field(models.Model):
    fieldName = models.CharField(max_length=150)

class Lawyers(models.Model):
    img=models.ImageField(upload_to='Lawyers')
    name = models.CharField(max_length=150)
    lawSchool = models.CharField(max_length=150)
    recognisedSince = models.IntegerField()
    phone = models.IntegerField()
    languages = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    bio = models.TextField()
    field = models.CharField(max_length=150)