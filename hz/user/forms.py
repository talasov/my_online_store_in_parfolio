from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class UserRegisterForm(UserCreationForm):
    """Форма регистрации пользователя"""
    username = forms.CharField(min_length=6, max_length=30,
                               widget=forms.TextInput(attrs={'class': 'contactus',
                                                             'placeholder': 'Логин'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'contactus',
                                                            'placeholder': 'E-mail'}))

    first_name = forms.CharField(max_length=50, min_length=2,
                                 widget=forms.TextInput(attrs={'class': 'contactus',
                                                               'placeholder': 'Ваше имя'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'contactus',
                                                                  'placeholder': 'Придумайте пароль'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'contactus',
                                                                  'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    """Форма входа пользователя"""
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'contactus',
                                                             'placeholder': 'Логин'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'contactus',
                                                                 'placeholder': 'Введите пароль'}))
