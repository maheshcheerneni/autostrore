# Generated by Django 4.1.3 on 2022-11-19 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BikeStore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bikemodels',
            name='description',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bikemodels',
            name='launch_Date',
            field=models.DateField(),
        ),
    ]
