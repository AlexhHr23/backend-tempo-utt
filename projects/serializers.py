from rest_framework import serializers
from .models import *

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class ClassAcademySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassAcademy
        fields = '__all__'

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id','name','last_name']

class ScheduleSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(many=True)
    class Meta:
        model = Schedule
        fields = '__all__'
