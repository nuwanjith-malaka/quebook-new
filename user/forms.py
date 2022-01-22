from django import forms
from user.models import AskerProfile

class AskerProfileForm(forms.ModelForm):
    class Meta:
        model = AskerProfile
        exclude = ['user']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'photo': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Photo'}),
            'age': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'Website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Website'}),
        }