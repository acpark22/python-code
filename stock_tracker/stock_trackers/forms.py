from django import forms
from .models import Stock, Entry

class StockForm(forms.ModelForm):
    class Meta:
        model= Stock
        fields= ['text']
        labels= {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model= Entry
        fields= ['text']
        labels= {'text': 'Entry:'}
        widgets= {'text': forms.Textarea(attrs={'cols': 80})}

