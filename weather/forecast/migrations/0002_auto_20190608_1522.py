# Generated by Django 2.2.2 on 2019-06-08 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forecast', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accurateforecast',
            name='date',
            field=models.DateField(),
        ),
    ]
