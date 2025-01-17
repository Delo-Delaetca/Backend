from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Делаем фому регистрациии пользователя

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=60, required=True,)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Пользователь с таким email уже существует.')
        return email

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


# А тут делаем фому для изменения пользователя

class UserEditForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True,)
    email = forms.EmailField(max_length=60, required=True,)
    
    def clean_username(self):
        name = self.cleaned_data.get('username')
        if User.objects.filter(username=name).exclude(pk=self.instance.pk).exists():
            raise ValidationError('Пользователь с таким name уже существует.')
        return name
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError('Пользователь с таким email уже существует.')
        return email
    
    class Meta:
        model = User
        fields = ("username", "email",)