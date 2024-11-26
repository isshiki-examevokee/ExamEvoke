from .students.viewsets import (
    StudentViewset,
)

from .users.viewsets import (
    EmployeeViewset,
    CustomAuthTokenView,
)

from .courses.viewset import (
    CourseViewset,
)

from .subjects.viewset import (
    SubjectViewset
)

from .batches.viewset import (
    BatchViewset
)

from .topics.viewset import (
    TopicViewset
)



__all__ = [
    "StudentViewset",
    "EmployeeViewset",
    "CustomAuthTokenView",
    "CourseViewset",
    "SubjectViewset",
    "BatchViewset",
    "TopicViewset",
]