from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    zipcode = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'zipcode', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    zipcode = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #date_joined = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #last_login = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #is_superuser = forms.CharField(max_length=50, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    #is_staff = forms.CharField(max_length=50, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    #is_active = forms.CharField(max_length=50, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'zipcode', 'username', 'password')