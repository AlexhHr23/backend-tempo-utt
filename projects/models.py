from django.contrib import admin
from django.db import models
from django.core.validators import MinValueValidator

class Subject(models.Model):
    name = models.CharField('Nombre', max_length=100, blank=True)
    color = models.CharField('Color', max_length=7, default='FFFFFFF')
    description = models.TextField('Descripción', blank=True)
    

    def __str__(self):
        return self.name
    
class Group(models.Model):
    
    shift_choices = [
        ('Matutino', 'Matutino'),
        ('Vespertino', 'Vespertino'),
    ]
    
    name = models.CharField( 'Nombre', max_length=50, blank=True)
    shift = models.CharField('Turno', max_length=20, choices=shift_choices, default='Matutino')
    
    def __str__(self):
        return f'{self.name} {self.shift}'
    
class ClassAcademy(models.Model):
    name = models.CharField('Nombre', max_length=100, blank=True, unique=True)
    color = models.CharField('Color', max_length=7, default='FFFFFFF')
    groups = models.ForeignKey(Group, on_delete=models.CASCADE, default=1)
    
    
    def __str__(self):
        return f'{self.name}'
    
class Building(models.Model):
    name = models.CharField('Nombre', max_length=100, blank=True)
    
    def __str__(self):
        return self.name

class Classroom(models.Model):
    
    type_choices = [
        ('Aula Compartida', 'Aula Compartida'),
        ('Aula fija', 'Aula fija')
    ]
    
    name = models.CharField('Nombre', max_length=100, blank=True)
    rol = models.CharField('Tipo de aula', max_length=20, choices=type_choices, default='Aula compartida')
    color = models.CharField('Color', max_length=7, default='FFFFFFF')
    building = models.ForeignKey(Building, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


    
class Teacher(models.Model):
    
    name = models.CharField('Nombre', max_length=100, blank=True)
    last_name = models.CharField('Apellido', max_length=100, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField('Número telefónico', max_length=10, unique=True, blank=True)
    color = models.CharField('Color', max_length=7, default='FFFFFFF')
    session_week = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    lessons_day = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    class_academy = models.ManyToManyField(ClassAcademy) 
    classroom_assigned = models.ForeignKey(Classroom, on_delete=models.CASCADE, null=True, blank=True)

    
    

    def __str__(self):
       return f'{self.name} - {self.last_name}'
   
class Schedule(models.Model):
    number_days = models.IntegerField('Numero de dias')
    hour_start = models.TimeField('Hora inicio', blank=True)
    hour_end = models.TimeField('Hora fin', blank=True)
    teacher = models.ManyToManyField(Teacher)
    

    def __str__(self):
        return f'{self.four_month_period} - {self.number_days} - {self.day_week}: {self.hour_start} - {self.hour_end} - {self.teacher}'