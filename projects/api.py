from projects.models import *
from rest_framework import viewsets, permissions
from .serializers import *

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SubjectSerializer

class CareerViewSet(viewsets.ModelViewSet):
    queryset = Career.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CareerSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GroupSerializer

class ClassAcademyViewSet(viewsets.ModelViewSet):
    queryset = ClassAcademy.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClassAcademySerializer

class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BuildingSerializer

class ClassRoomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClassroomSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TeacherSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ScheduleSerializer
    
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = StudentSerializer