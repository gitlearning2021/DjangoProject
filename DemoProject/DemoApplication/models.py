from django.db import models

# Create your models here.
class Location(models.Model):
    id=models.IntegerField(primary_key=True)
    value=models.CharField(max_length=30)

class Book(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)