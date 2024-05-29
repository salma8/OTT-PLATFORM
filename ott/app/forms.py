from django import forms
from .models import Movie, Subscription


class MyLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['plan']


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

