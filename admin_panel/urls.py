from django.urls import include, path
from rest_framework import routers

from admin_panel.viewsets import BatchViewset, CourseViewset

router = routers.DefaultRouter()
router.register(r"course", CourseViewset, basename="course")
router.register(r"batch", BatchViewset, basename="batch")
urlpatterns = [path("", include(router.urls))]
