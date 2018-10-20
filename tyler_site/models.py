# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='images')

    def __unicode__(self):
        return self.name


class Testimonial(models.Model):
    client = models.CharField(max_length=400, null=True, blank=True)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='images/logos')

    testimonial = models.TextField()

    def __unicode__(self):
        return self.name