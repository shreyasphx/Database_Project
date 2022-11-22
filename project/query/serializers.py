#serializer.py

from rest_framework import serializers

from .models import Query

class QuerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Query
        fields = ('name','query', 'connection')