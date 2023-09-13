from rest_framework import routers
from .api import *

router = routers.DefaultRouter()

router.register('api/subjects', SubjectViewSet, 'subjects')
router.register('api/careers', CareerViewSet, 'careers') 
router.register('api/groups', GroupViewSet, 'groups')
router.register('api/classacademies', ClassAcademyViewSet, 'classacademies')
router.register('api/buildings', BuildingViewSet, 'buildings')
router.register('api/classrooms', ClassRoomViewSet, 'classrooms')
router.register('api/teachers', TeacherViewSet, 'teachers')
router.register('api/schedules', ScheduleViewSet, 'schedules')
router.register('api/students', StudentViewSet, 'students')

urlpatterns = router.urls



