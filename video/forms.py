from django import forms
from .models import Calendar

class DateInput(forms.DateInput):
    input_type = 'date'


class CalendarForm(forms.ModelForm):
    title = forms.CharField()
    content = forms.CharField()

    class Meta:
            model = Calendar
            fields = ['date_from', 'date_to', 'title', 'content', 'link']
            widgets = {
                'date_from' : DateInput(),
                'date_to' : DateInput()
            }
