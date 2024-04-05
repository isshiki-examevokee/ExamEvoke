from django.urls import include, path
from rest_framework import routers

from admin_panel.viewsets import (
    BatchViewset,
    CourseViewset,
    OrganizationViewset,
    SubjectViewset,
    TopicViewset,
)

router = routers.DefaultRouter()
router.register(r"course", CourseViewset, basename="course")
router.register(r"batch", BatchViewset, basename="batch")
router.register(r"organization", OrganizationViewset, basename="organization")
router.register(r"subject", SubjectViewset, basename="subject")
router.register(r"topic", TopicViewset, basename="topic")
urlpatterns = [path("", include(router.urls))]
