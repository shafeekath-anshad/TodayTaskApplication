from django import forms
from .models import today_task


class todayform(forms.ModelForm):
    class Meta:
        model = today_task
        fields = ['Take_name', 'priority', 'date']
