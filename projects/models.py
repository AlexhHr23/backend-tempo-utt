from django.contrib import admin
from django.db import models
from django.core.validators import MinValueValidator

class Subject(models.Model):
    name = models.CharField('Nombre', max_length=100, blank=True)
    color = models.CharField('Color', max_length=7, default='FFFFFFF')
    description = models.TextField('Descripción', blank=True)
    

    def __str__(self):
        return self.name

class Career(models.Model):
    name = models.CharField('Nombre de la Carrera', max_length=100)
    description = models.TextField('Descripción de la Carrera', blank=True)

    def __str__(self):
        return self.name
    
class Group(models.Model):
    name = models.CharField( 'Nombre', max_length=50, blank=True)
    shift = models.CharField('Turno', max_length=20, blank=True)
    Career = models.ForeignKey(Career, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return f'{self.name} {self.shift}'
    
class ClassAcademy(models.Model):
    name = models.CharField('Nombre', max_length=100, blank=True, unique=True)
    color = models.CharField('Color', max_length=7, default='FFFFFFF')
    groups = models.ForeignKey(Group, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'{self.name}'
    
class Building(models.Model):
    name = models.CharField('Nombre', max_length=100, blank=True)
    
    def __str__(self):
        return self.name

class Classroom(models.Model):
    
    name = models.CharField('Nombre', max_length=100, blank=True)
    rol = models.CharField('Tipo de aula', max_length=20, blank = True)
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
    tuition = models.CharField('Matrícula', max_length=12, blank=True)
    password = models.CharField('Contraseña', max_length=20, blank=True)
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
    classroom = models.ManyToManyField(Classroom) 
    

    def __str__(self):
        return f'{self.four_month_period} - {self.number_days} - {self.day_week}: {self.hour_start} - {self.hour_end} - {self.teacher}'

class Student(models.Model):
    first_name = models.CharField('Nombre', max_length=100, blank=True)
    last_name = models.CharField('Apellido', max_length=100, blank=True)
    email = models.EmailField('Correo Electrónico', unique=True)
    student_id = models.CharField('Número de Estudiante', max_length=10, unique=True, blank=True)
    tuition = models.CharField('Matrícula', max_length=12, blank=True)
    password = models.CharField('Contraseña', max_length=20, blank=True)
    Schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'