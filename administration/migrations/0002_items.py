# Generated by Django 5.1.2 on 2024-11-04 00:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('origin', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('image', models.URLField(max_length=255)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.supplier')),
            ],
        ),
    ]
