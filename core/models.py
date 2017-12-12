from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Scheduling(models.Model):
    class Meta:
        verbose_name = _('agendamento')
        verbose_name_plural = _('agendamentos')

    patient = models.CharField(_('paciente'), max_length=20)
    procedure = models.CharField(_('procedimento'), max_length=30)
    date = models.DateField(_('dia da consulta'))
    start_time = models.TimeField(_('inicio'))
    end_time = models.TimeField(_('fim'))
    created_at = models.DateTimeField(_('criado em'), default=timezone.now)

    #def __str__(self):
    #   return f'Das {self.start_time} até {self.end_time} realização de {self.procedure}'.capitalize()
