from django.db import models

# Create your models here.

class Course(models.Model):
  title = models.CharField(max_length=100)
  image = models.CharField(max_length=700)

  def __str__(self):
    return self.title
  
class Project(models.Model):
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=100)
  image = models.CharField(max_length=700)
  url = models.CharField(max_length=200)
  tec = models.CharField(max_length=100)

  def __str__(self):
    return self.title

class Session(models.Model):
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=100)

  def __str__(self):
    return self.title
