# Generated by Django 5.0.7 on 2024-07-23 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0005_alter_activitiesmodel_activity_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitiesmodel',
            name='activity_img',
            field=models.ImageField(upload_to='static'),
        ),
    ]
