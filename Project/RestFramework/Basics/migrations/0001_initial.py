# Generated by Django 5.1.3 on 2024-11-29 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='basics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('about', models.TextField()),
                ('gender', models.CharField(choices=[('male', True), ('female', False), ('None', None)], max_length=50)),
                ('salary', models.FloatField()),
                ('married', models.BooleanField()),
                ('dateOfJoin', models.DateField()),
                ('insertTime', models.DateTimeField()),
            ],
        ),
    ]
