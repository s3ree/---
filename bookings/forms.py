from django import forms
from .models import UserProfile, Booking

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'phone', 'company_name']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['company_name', 'start_date', 'end_date', 'number_of_cookers']

    start_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

