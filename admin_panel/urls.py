from django.urls import include, path
from rest_framework import routers

from admin_panel.questions.viewset import QuestionViewset

from admin_panel.students.viewset import StudentViewset
from admin_panel.viewset import (
    CustomAuthTokenView,
    EmployeeViewset,
    CourseViewset,
    SubjectViewset,
    BatchViewset,
    TopicViewset,
    OrganizationViewset,
    ExamViewSet,
    ExamBatchViewSet,
    ExamStudentViewSet,
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
router.register(r"exam", ExamViewSet, basename="exam")
router.register(r"exam_batch", ExamBatchViewSet, basename="exam_batch")
router.register(r"exam_student", ExamStudentViewSet, basename="exam_student")
urlpatterns = [path("", include(router.urls))]
urlpatterns += [path('api-token-auth/', CustomAuthTokenView.as_view())]
