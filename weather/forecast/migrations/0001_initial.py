# Generated by Django 2.2.2 on 2019-06-08 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeasonForecast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('mean_temperature', models.IntegerField()),
                ('median_temperature', models.IntegerField()),
                ('mode_temperature', models.IntegerField()),
                ('precipitation', models.CharField(choices=[('D', 'Dry'), ('A', 'Average'), ('W', 'Wet')], max_length=1)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seasons_forecasts', to='locations.Region')),
            ],
        ),
        migrations.CreateModel(
            name='AccurateForecast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(editable=False)),
                ('wind_direction', models.CharField(choices=[('N', 'North'), ('E', 'East'), ('S', 'South'), ('W', 'West'), ('NE', 'North-East'), ('SE', 'South-East'), ('NW', 'North-West'), ('SW', 'South-West')], max_length=2)),
                ('wind_speed', models.FloatField()),
                ('temperature', models.IntegerField()),
                ('precipitation', models.FloatField()),
                ('locality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forecasts', to='locations.Locality')),
            ],
        ),
    ]