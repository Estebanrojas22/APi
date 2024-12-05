from django.db import models

# Create your models here (tablas o colecciones)

class programmer(models.Model):
    fullname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=30)
    age = models.PositiveBigIntegerField(default=True)
    Phone = models.CharField(max_length= 10, null=True, default= None)
    is_active = models.BooleanField(default=True)

class Student(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    sexo = models.CharField(max_length=1)
    N_ficha = models.IntegerField(max_length=7)
    formacion = models.BooleanField(default=True)
    f_ingreso = models.DateField(default=None)


  