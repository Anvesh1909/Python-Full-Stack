# Generated by Django 5.1.6 on 2025-04-05 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('amount', models.IntegerField()),
                ('payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('order_id', models.CharField(max_length=100)),
                ('signature', models.CharField(blank=True, max_length=255, null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
