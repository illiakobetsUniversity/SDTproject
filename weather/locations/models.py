from django.db import models
from django.db.models.base import ModelBase

from abstractions import Observable


class Country(models.Model):
    class Meta:
        verbose_name_plural = 'Countries'

    title = models.CharField(max_length=256, null=False, blank=False)
    population = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return str(self.title)


class Region(models.Model):

    title = models.CharField(max_length=256, null=False, blank=False)
    country = models.ForeignKey('locations.Country', on_delete=models.CASCADE, related_name='regions')

    def __str__(self):
        return '{}, {}'.format(str(self.title), str(self.country))


class District(models.Model):

    title = models.CharField(max_length=256, null=False, blank=False)
    region = models.ForeignKey('locations.Region', on_delete=models.CASCADE, related_name='districts')

    def __str__(self):
        return '{}, region {}'.format(str(self.title), str(self.region))


class Locality(models.Model):
    class Meta:
        verbose_name_plural = "Localities"

    title = models.CharField(max_length=256, null=False, blank=False)
    district = models.ForeignKey("locations.District", on_delete=models.CASCADE, related_name='localities')

    def __str__(self):
        return "{}, district {}".format(str(self.title), str(self.district))

    def subscribe(self, subscriber):
        self.subscriptions.add(subscriber)

    def unsubscribe(self, subscriber):
        if subscriber in self.subscriptions:
            self.subscriptions.remove(subscriber)

    def notify_all(self):
        for user in self.subscriptions:
            user.notify(self)
