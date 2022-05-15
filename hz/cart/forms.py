from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]


class CartAddProductForm(forms.Form):
    """Форма кол-ва и изменения кол-ва товара"""
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        label='Кол-во'
    )
    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput(attrs={'class': 'nice-select'})
    )
