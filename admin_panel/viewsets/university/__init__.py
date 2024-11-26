from ...batches.viewset import BatchViewset
from ...courses.viewset import CourseViewset
from .organization import OrganizationViewset
from ...subjects.viewset import SubjectViewset
from .topic import TopicViewset
# from ..user.employee import EmployeeViewset

__all__ = [
    "CourseViewset",
    "BatchViewset",
    "OrganizationViewset",
    "SubjectViewset",
    "TopicViewset",
]
