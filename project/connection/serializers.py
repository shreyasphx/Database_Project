#serializer.py

from rest_framework import serializers

from .models import Connection

class ConnectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Connection
        fields = ('dbname', 'user', 'password', 'host', 'port')