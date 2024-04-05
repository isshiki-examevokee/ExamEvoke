from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r"user", core_views.user.UserViewSet, basename="user")
urlpatterns = [path("", include(router.urls))]
