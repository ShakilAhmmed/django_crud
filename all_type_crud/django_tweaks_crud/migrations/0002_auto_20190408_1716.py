# Generated by Django 2.2 on 2019-04-08 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_tweaks_crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crudwithtweaks',
            name='category_status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=20),
        ),
    ]
