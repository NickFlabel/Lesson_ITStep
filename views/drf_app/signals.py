from django.dispatch import Signal
from django.dispatch import receiver

my_signal = Signal()

@receiver(my_signal)
def my_func(sender, **kwargs):
    print('signal')


my_signal.send()
