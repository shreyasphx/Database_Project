# Generated by Django 4.1.3 on 2022-11-22 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('connection', '0001_initial'),
        ('query', '0002_query_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='connection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='connection.connection'),
        ),
    ]