from django.db import models


class AccurateForecast(models.Model):

    wind_directions_choices = (
        ('N', 'north'),
        ('E', 'east'),
        ('S', 'south'),
        ('W', 'west'),
        ('NE', 'north-east'),
        ('SE', 'south-east'),
        ('NW', 'north-west'),
        ('SW', 'south-west'),
    )

    locality = models.ForeignKey('locations.Locality', on_delete=models.CASCADE, related_name='forecasts')
    date = models.DateField(editable=True, null=False, blank=False)
    wind_direction = models.CharField(max_length=2, choices=wind_directions_choices, null=False, blank=False)
    wind_speed = models.FloatField(null=False, blank=False)
    temperature = models.IntegerField(null=False, blank=False)
    precipitation = models.FloatField(null=False, blank=False)

    def __str__(self):
        string_args = self.temperature, self.wind_speed, self.get_wind_direction_display(), self.locality, self.date
        return '{}C, {} {} wind, {}, {}'.format(*string_args)


class SeasonForecast(models.Model):

    seasons_choices = (
        ('WI', 'winter'),
        ('SP', 'spring'),
        ('SU', 'summer'),
        ('AU', 'autumn'),
    )

    precipitation_choices = (
        ('D', 'dry'),
        ('A', 'average'),
        ('W', 'wet'),
    )

    year = models.IntegerField(null=False, blank=False)
    region = models.ForeignKey("locations.Region", on_delete=models.CASCADE, related_name='seasons_forecasts')
    mean_temperature = models.IntegerField(null=False, blank=False)
    median_temperature = models.IntegerField(null=False, blank=False)
    mode_temperature = models.IntegerField(null=False, blank=False)
    precipitation = models.CharField(max_length=1, choices=precipitation_choices)
    season = models.CharField(max_length=2, choices=seasons_choices)

    def __str__(self):
        string_args = self.region, self.get_season_display(), self.year
        return '{},  {} {} season forecast'.format(*string_args)
