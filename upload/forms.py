from django import forms
from django.contrib.auth import get_user_model
from .models import Upload

User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        foo = User.objects.filter(username=username)
        if foo.exist():
            raise forms.ValidationError("Username is already taken")
        return email

    def clean_email(self):
        email = self.cleaned_data.get('email')
        foo = User.objects.filter(email=email)
        if foo.exist():
            raise forms.ValidationError("Email is already taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password2 != password:
            raise forms.ValidationError("Password are not a match")
        return data
class UploadModelForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = [
            'user',
            'content'
        ]

        def clean_content(self):
            data = self.cleaned_data('content')
            if data == 'abc':
                raise forms.ValidationError("Cannot be abc")

            return data