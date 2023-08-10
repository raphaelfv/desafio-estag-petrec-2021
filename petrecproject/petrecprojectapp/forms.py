from django import forms
from .models import Feedback

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(label='Upload CSV file')

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'text']