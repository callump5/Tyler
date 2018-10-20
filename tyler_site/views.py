# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Service, Testimonial



# Create your views here.

def get_base(request):
    services = Service.objects.all()[:3]
    testimonials = Testimonial.objects.all()
    args = {'services': services,
            'testimonials': testimonials}
    return render(request, 'index.html', args)
