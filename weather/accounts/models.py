from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import ModelBase
from abstractions import Observer


class User(AbstractUser):

    locality = models.ForeignKey('locations.Locality', on_delete=models.SET_NULL, null=True, related_name='residents')
    localities_subscriptions = models.ManyToManyField('locations.Locality', related_name='subscriptions')

    def notify(self, *args, **kwargs):
        string_args = self.username
        print('User {} is notified about weather conditions'.format(*string_args))
