from django import forms

class CreateInputForm(forms.Form):
    text_input = forms.CharField(label='text-task', max_length=100)