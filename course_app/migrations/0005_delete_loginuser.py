# Generated by Django 3.2.2 on 2021-05-19 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0004_loginuser_islogin'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Loginuser',
        ),
    ]
