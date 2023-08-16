from django.db import models

class Subject(models.Model):
    name = models.CharField('Nombre', max_length=100, blank=True)
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
    
    def __str__(self):
        return f'{self.name}'
    
class Building(models.Model):
    name = models.CharField('Nombre', max_length=100, blank=True)
    
    def __str__(self):
        return self.name

class Classroom(models.Model):
    name = models.CharField('Nombre', max_length=100, blank=True)
    rol_classroom = models.BooleanField(default=False)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


    
class Teacher(models.Model):
    
    name = models.CharField('Nombre', max_length=100, blank=True)
    last_name = models.CharField('Apellido', max_length=100, blank=True)
    email = models.EmailField()
    phone_number = models.CharField('Número telofónico', max_length=10, blank=True)
    session_week = models.IntegerField(default=1)
    lessons_day = models.IntegerField(default=1)
    class_academy = models.ForeignKey(ClassAcademy, on_delete=models.CASCADE, default=1)
    subjects_taught = models.ManyToManyField(Subject)
    classrooms_assigned = models.ManyToManyField(Classroom)
    
    

    def __str__(self):
        return f'{self.name} - {self.last_name} - {self.subjects_taught} - {self.teacher} - {self.classroom}'

    

class Schedule(models.Model):
    number_days = models.IntegerField('Numero de dias')
    hour_start = models.TimeField('Hora inicio', blank=True)
    hour_end = models.TimeField('Hora fin', blank=True)
    teacher = models.ManyToManyField(Teacher)
    

    def __str__(self):
        return f'{self.four_month_period} - {self.number_days} - {self.day_week}: {self.hour_start} - {self.hour_end} - {self.teacher}'

    