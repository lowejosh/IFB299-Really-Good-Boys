# Imports
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Sign up form (additional) fields
class SignUpForm(UserCreationForm):
    firstName = forms.CharField(label='First Name', required=True)   # Note for later: help_text can be an additional parameter
    lastName = forms.CharField(label='Last Name', required=True)
    gender = forms.ChoiceField(choices=[(1, "Male"), (2, "Female"), (3, "Other")])
    accountType = forms.ChoiceField(label='Account Type', choices=[(1, "Student"), (2, "Business"), (3, "Tourist")])
    dateOfBirth = forms.DateField(label='Date of Birth', required=True, widget=forms.TextInput(attrs={'placeholder': 'mm/dd/yyy'}))
    email = forms.EmailField(label='Email Address', required=True, widget=forms.TextInput(attrs={'placeholder': 'example@email.com'}))
    phoneNumber = forms.RegexField(label='Phone Number', regex=r'^\+?1?\d{9,15}$', required=False)
    address = forms.CharField(label='Home Address', required=True)

    class Meta:
        model = User
        fields = ('username', 'firstName', 'lastName', 'gender', 'accountType', 'email', 'dateOfBirth', 'phoneNumber', 'address', 'password1', 'password2', )
    