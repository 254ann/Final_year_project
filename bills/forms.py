# In forms.py
from django import forms
from .models import BillReminder

class BillReminderForm(forms.ModelForm):
    class Meta:
        model = BillReminder
        fields = ['title', 'category', 'amount', 'due_date']
