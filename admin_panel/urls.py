from django.urls import include, path
from rest_framework import routers

from admin_panel.viewsets import (
    BatchViewset,
    CourseViewset,
    OrganizationViewset,
    SubjectViewset,
    TopicViewset,
    EmployeeViewset,
    StudentViewset,
    CustomAuthTokenView,
    QuestionViewset,
    ExamViewset,
    ExamBatchViewset
)

router = routers.DefaultRouter()
router.register(r"course", CourseViewset, basename="course")
router.register(r"batch", BatchViewset, basename="batch")
router.register(r"organization", OrganizationViewset, basename="organization")
router.register(r"subject", SubjectViewset, basename="subject")
router.register(r"topic", TopicViewset, basename="topic")
router.register(r"employee", EmployeeViewset, basename="employee")
router.register(r"student", StudentViewset, basename="student")
router.register(r"question", QuestionViewset, basename="question")
router.register(r"exam", ExamViewset, basename="exam")
router.register(r"exam_batch", ExamBatchViewset, basename="exam_batch")
urlpatterns = [path("", include(router.urls))]
urlpatterns += [path('api-token-auth/', CustomAuthTokenView.as_view())]
