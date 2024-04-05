from django.urls import include, path
from rest_framework import routers

from admin_panel.viewsets import BatchViewset, CourseViewset, OrganizationViewset

router = routers.DefaultRouter()
router.register(r"course", CourseViewset, basename="course")
router.register(r"batch", BatchViewset, basename="batch")
router.register(r"organization", OrganizationViewset, basename="organization")
urlpatterns = [path("", include(router.urls))]
