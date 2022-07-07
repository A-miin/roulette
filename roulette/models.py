from django.contrib.auth.models import Group as UserRole
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import F
from django.utils.translation import gettext_lazy as _
import random


class Roulette(models.Model):
    value = models.IntegerField()
    weight = models.IntegerField(default=1)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = _('Номер рулетки')
        verbose_name_plural = _('Номера рулетки')


class Round(models.Model):
    number = models.IntegerField()
    used_numbers = models.ManyToManyField(
        'roulette.Roulette',
        related_name='rounds'
    )
    users = models.ManyToManyField(
        get_user_model(),
        related_name='users'
    )
    finish = models.BooleanField(default=False)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = _('Раунд')
        verbose_name_plural = _('Раунды')

    def get_roulette_number(self) -> Roulette:
        roulettes = Roulette.objects.exclude(id__in=F("used_numbers")).exclude(value=-1)
        roulettes_weight_list = []
        for roulette in roulettes:
            roulettes_weight_list.extend([roulette]*roulette.weight)

        if not roulettes_weight_list:
            return Roulette.objects.get(value=-1)

        return random.choice(roulettes_weight_list)
