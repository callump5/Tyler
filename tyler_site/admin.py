# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from . models import Service, Testimonial, CallBooking

# Register your models here.

admin.site.register(Service)
admin.site.register(Testimonial)
admin.site.register(CallBooking)
