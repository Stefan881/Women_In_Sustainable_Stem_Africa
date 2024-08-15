from django import forms
from django.contrib.auth.models import User
from tinymce.widgets import TinyMCE


class NewsletterForm(forms.Form):
    subject = forms.CharField()
    receivers = forms.CharField()
    message = forms.CharField(widget=TinyMCE(),label="Email content")