from django import forms
from .models import Movie

#from .models import Subscription


class MyLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


'''class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['customer', 'plan', 'start_date']
'''



class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

