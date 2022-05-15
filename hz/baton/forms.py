from django import forms
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    """Форма обратной связи"""
    name = forms.CharField(
        label='Ваше имя',
        min_length=2,
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'contactus',
            'placeholder': 'Ваше имя'
        })
    )
    phone = forms.CharField(
        label='Номер телефона',
        max_length=15,
        min_length=10,
        help_text='Укажите в формате: +7 000 000-00-00',
        widget=forms.TextInput(attrs={'class': 'contactus',
                                      'placeholder': 'Номер телефона'
                                      })
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'contactus',
            'placeholder': 'E-mail'
        })
    )
    message = forms.CharField(
        label='Сообщение',
        help_text='Введите текст',
        widget=forms.Textarea(attrs={
            'class': 'textarea',
            'placeholder': 'Сообщение...'
        })
    )
    captcha = CaptchaField()
