from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ClimaticDataForm(forms.Form):
    temperature = forms.FloatField(label='Temperature')
    humidity = forms.FloatField(label='Humidity')
    wind_speed = forms.FloatField(label='Wind Speed')
    # Add more fields as needed for your prediction
