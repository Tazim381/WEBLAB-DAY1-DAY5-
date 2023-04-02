# Generated by Django 4.0.5 on 2022-11-24 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=100, unique=True)),
                ('emp_name', models.CharField(max_length=50)),
                ('dept', models.CharField(max_length=150)),
            ],
        ),
    ]