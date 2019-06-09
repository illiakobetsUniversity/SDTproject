from django.contrib import admin

from .models import AccurateForecast, SeasonForecast


admin.site.register(AccurateForecast)
admin.site.register(SeasonForecast)
