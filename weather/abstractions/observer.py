from abc import ABCMeta, abstractmethod


__all__ = ['Observer', 'Observable']


class Observer:

    @abstractmethod
    def notify(self, *args, **kwargs):
        pass


class Observable(metaclass=ABCMeta):

    @abstractmethod
    def notify_all(self):
        pass

    def subscribe(self, subscriber: Observer):
        pass

    def unsubscribe(self, subscriber: Observer):
        pass



