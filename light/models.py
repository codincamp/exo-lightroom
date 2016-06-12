from __future__ import unicode_literals

from django.db import models

class Light(models.Model):
    LIGHT_COLOR_CHOICES = (
     ("FF0000", 'Rouge'),
     ("00FF00",'Vert'),
     ("0000FF",'Bleu'),
    )

    LIGHT_STATE_CHOICES = (
     (1, 'ON'),
     (0, 'OFF'),
    )

    color = models.CharField(max_length=6, choices=LIGHT_COLOR_CHOICES)
    state = models.IntegerField(choices=LIGHT_STATE_CHOICES)
