from django.db import models
from connection.models import Connection
# Create your models here.
class Query(models.Model):
    name = models.CharField(max_length=60)
    connection = models.ForeignKey(to=Connection, on_delete=models.DO_NOTHING, null = True)
    query = models.CharField(max_length=2048)

    def __str__(self):
        return self.name