# Generated by Django 3.2.2 on 2021-05-23 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0011_alter_course_teacherid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='studentnum',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
