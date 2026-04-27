from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeePsyCapViewSet

router = DefaultRouter()
router.register(r'employees', EmployeePsyCapViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
