# Generated by Django 3.2.4 on 2021-06-21 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Charity_app', '0004_donation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='zip_code',
            field=models.IntegerField(),
        ),
    ]
