from django.db import migrations,models
from django.contrib.auth.models import Group

def create_user_group(apps , schema_editor):

    Group.objects.create(name='student')
    Group.objects.create(name='profesor')
    Group.objects.create(name='admin')


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial')
    ]

    operations = [
        migrations.RunPython(create_user_group)
    ]