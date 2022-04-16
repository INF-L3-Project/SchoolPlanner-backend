from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class InstitutionSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True) 
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), required=True)
    institution_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    institution_logo = forms.ImageField(required=False)
    institution_description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'
        )
    

    def __init__(self, *args, **kwargs):
        super(InstitutionSignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


