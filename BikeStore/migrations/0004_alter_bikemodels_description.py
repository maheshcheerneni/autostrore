# Generated by Django 4.1.3 on 2022-11-20 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BikeStore', '0003_alter_bikemodels_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bikemodels',
            name='description',
            field=models.TextField(max_length=100),
        ),
    ]
