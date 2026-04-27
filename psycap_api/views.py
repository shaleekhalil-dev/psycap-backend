from rest_framework import viewsets
from .models import EmployeePsyCap
from .serializers import EmployeePsyCapSerializer

class EmployeePsyCapViewSet(viewsets.ModelViewSet):
    queryset = EmployeePsyCap.objects.all()
    serializer_class = EmployeePsyCapSerializer
