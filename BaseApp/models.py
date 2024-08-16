from django.db import models

# Create your models here.
class Guitar(models.Model):
  name = models.CharField(max_length=50)
  price = models.IntegerField()

class Bass(models.Model):
  name = models.CharField(max_length=50)
  price = models.IntegerField()

class Client(models.Model):
  name = models.CharField(max_length=50)
  surname = models.CharField(max_length=50)
  email = models.EmailField()
