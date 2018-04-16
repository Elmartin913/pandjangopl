from django import forms
from django.core.validators import validate_email
from .validators import phone_validator


from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'rows': 1, 'placeholder': '*Imie'}),
        max_length=128,
        required=True,
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={'rows': 1, 'placeholder': '*Email'}),
        max_length=128,
        validators = [validate_email],
        required=True,
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': '*Wiadomość'}),
        max_length=1024,
        required=True,
    )
    mobile = forms.CharField(
        widget=forms.TextInput(attrs={'rows': 1, 'type': 'number', 'placeholder': 'Telefon'}),
        validators=[phone_validator],
        required=False,
    )

    class Meta:
        model = Contact
        fields = [ 'name', 'email', 'mobile', 'message']
