# Generated by Django 3.2.20 on 2023-07-29 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eName', models.CharField(max_length=100)),
                ('eID', models.IntegerField()),
                ('eDesignation', models.CharField(max_length=100)),
                ('eJoiningDate', models.CharField(max_length=100)),
                ('eDepartment', models.CharField(max_length=100)),
                ('eSalary', models.IntegerField()),
                ('eExperience', models.IntegerField()),
            ],
        ),
    ]
