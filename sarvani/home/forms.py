from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback      # Tell Django to use our 'Feedback' model
        fields = ['name', 'comment'] # List the fields we want in our form
