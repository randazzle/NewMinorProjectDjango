from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Custom forms

class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length = 30, required = False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length = 30, required = False)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label=("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label=("Confirm Password"))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

    # email = forms.EmailField(max_length=254, help_text ='Required. Inform a valid email address')         WRONG LAYOUT FORMAT

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    def save(self, commit = True):
        user = super(RegistrationForm, self).save(commit = False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name  = self.cleaned_data['last_name']
        user.email      = self.cleaned_data['email']
        user.password1  = self.cleaned_data['password1']
        user.password2  = self.cleaned_data['password2']

        if commit:
            user.save()

        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
