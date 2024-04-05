from django.urls import include, path
from rest_framework import routers

from admin_panel.viewsets import CourseViewset

router = routers.DefaultRouter()
router.register(r"course", CourseViewset, basename="course")
urlpatterns = [path("", include(router.urls))]
