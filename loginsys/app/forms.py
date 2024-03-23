from app.models import *
from django import forms

class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
    class Meta:
        model = User 
        fields = ['username','email', 'password']
        widgets = {'password':forms.PasswordInput}
        lebels ={
            'Email Address':'Email'
        }
        


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['username','email']

