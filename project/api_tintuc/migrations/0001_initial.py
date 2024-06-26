# Generated by Django 5.0.4 on 2024-04-17 15:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Giaidau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenGD', models.CharField(max_length=100)),
                ('logoGD', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tintuc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tieude', models.CharField(max_length=100)),
                ('tomtat', models.CharField(max_length=100)),
                ('noidung', models.CharField(max_length=1000)),
                ('hinhanh', models.CharField(max_length=100)),
                ('tacgia', models.CharField(max_length=100)),
                ('ngaydang', models.DateTimeField(auto_now_add=True)),
                ('giaidau', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api_tintuc.giaidau')),
            ],
        ),
    ]
