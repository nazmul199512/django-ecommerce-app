from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name', 'email', 'subject', 'message'
        ]
        labels = {
           "name": "Your Name",
            "email": "Your Email",
            "subject": "Subject",
            "message": "Message"
        }