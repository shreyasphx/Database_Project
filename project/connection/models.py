from django.db import models

# Create your models here.
class Connection(models.Model):
    dbname = models.CharField(max_length=60)
    user = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    host = models.CharField(max_length=60)
    port = models.IntegerField()

    def __str__(self):
        return self.dbname