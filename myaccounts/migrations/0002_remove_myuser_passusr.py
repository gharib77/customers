# Generated by Django 3.2 on 2021-06-15 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myaccounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='passusr',
        ),
    ]
