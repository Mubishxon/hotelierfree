from django import forms
from .models import Newsletter, Contact

class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = "__all__"

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"
