# Generated by Django 5.1.2 on 2024-11-06 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0004_alter_supplier_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameters',
            name='value',
            field=models.IntegerField(),
        ),
    ]
