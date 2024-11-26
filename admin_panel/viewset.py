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


__all__ = [
    "StudentViewset",
    "EmployeeViewset",
    "CustomAuthTokenView",
    "CourseViewset",
]