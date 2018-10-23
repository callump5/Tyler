# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.db import models

from datetime import time

# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=300)
    image_1 = models.ImageField(upload_to='images')
    image_2 = models.ImageField(upload_to='images', help_text='Not required', null=True, blank=True)
    image_3 = models.ImageField(upload_to='images', help_text='Not required', null=True, blank=True)


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


class CallBooking(models.Model):
    name = models.CharField(max_length=300)
    number = models.CharField(max_length=14)
    email = models.CharField(max_length=300)

    TIME_CHOICES = (
        (time(9, 00, 00), u'9 AM'),
        (time(10, 00, 00), u'10 AM'),
        (time(11, 00, 00), u'11 AM'),
        (time(12, 00, 00), u'12 PM'),
        (time(13, 00, 00), u'1 PM'),
        (time(14, 00, 00), u'2 PM'),
        (time(15, 00, 00), u'3 PM'),
        (time(16, 00, 00), u'4 PM'),
        (time(17, 00, 00), u'5 PM'),
    )

    booking_time = models.TimeField(u'Booking time', choices=TIME_CHOICES)

    day = models.DateField(u'Booking date')

    def __unicode__(self):
        return self.name


    def clean(self):
        events = CallBooking.objects.filter(day=self.day, booking_time=self.booking_time)

        if events:
            raise ValidationError('There is currently a booking for this time!')