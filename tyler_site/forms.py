from django import forms

from .models import CallBooking

class CallForm(forms.ModelForm):
    class Meta:
        model = CallBooking
        fields = ['name', 'number', 'email', 'booking_time', 'day']

        day = forms.DateField(
            widget=forms.widgets.DateInput(format="%m/%d/%Y"))