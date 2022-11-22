#views.py

from rest_framework import viewsets

from .serializers import QuerySerializer
from .models import Query

class QueryViewSet(viewsets.ModelViewSet):
    queryset = Query.objects.all().order_by('name')
    serializer_class = QuerySerializer
