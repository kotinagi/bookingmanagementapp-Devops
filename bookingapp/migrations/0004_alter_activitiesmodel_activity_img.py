# Generated by Django 4.2.11 on 2024-04-07 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookingapp", "0003_alter_bookedactivity_date_of_booking"),
    ]

    operations = [
        migrations.AlterField(
            model_name="activitiesmodel",
            name="activity_img",
            field=models.ImageField(upload_to="media"),
        ),
    ]