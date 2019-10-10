from django import forms

from .models import itemLI

class CreateInputForm(forms.Form):
    text_input = forms.CharField(label='text-task', max_length=100)

    def save(self):
        post = itemLI(len(itemLI.objects.order_by('id')[:])+1, False, self.text_input)