# Generated by Django 4.2.7 on 2023-11-25 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_Id', models.CharField(max_length=6)),
                ('employee_name', models.CharField(max_length=50)),
                ('salary', models.CharField(max_length=20)),
            ],
        ),
    ]