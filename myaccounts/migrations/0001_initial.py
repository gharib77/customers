# Generated by Django 3.2 on 2021-06-15 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Myuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('ut_name', models.CharField(max_length=100, unique=True)),
                ('prenom', models.CharField(blank=True, max_length=100)),
                ('passuser', models.CharField(max_length=100)),
                ('passusr', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]