#views.py

from rest_framework import viewsets

from .serializers import ConnectionSerializer
from .models import Connection

# Create your views here.
class ConnectionViewSet(viewsets.ModelViewSet):
    queryset = Connection.objects.all().order_by('dbname')
    serializer_class = ConnectionSerializer