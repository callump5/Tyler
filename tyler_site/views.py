# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse

from django.contrib import messages
from .models import Service, Testimonial
from .forms import CallForm



# Create your views here.



# Home View
def get_base(request):
    services = Service.objects.all()[:3]
    testimonials = Testimonial.objects.all()

    if request.method == 'POST':
        form = CallForm(request.POST)
        if form.is_valid():
            form.save()
            date = form.cleaned_data['day']
            time = form.cleaned_data['booking_time']
            messages.success(request, 'Thank you! You have booked a call for the: ' + str(date) + ' on: ' + str(time))
            return redirect('home')
        else:
            messages.error(request, 'Sorry there is currently another booking!')

    else:
        form = CallForm

    args = {'services': services,
            'testimonials': testimonials,
            'form':form}
    return render(request, 'home-page.html', args)




# Services View
def get_services(request):
    services = Service.objects.all()
    args = {'services': services}
    return render(request, 'services/services_page.html', args)

def get_service(request, service_id):
    service = Service.objects.get(id=service_id)
    args = {'service':service}
    return render(request, 'services/services_page.html', args)