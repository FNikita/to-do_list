from django import forms

from .models import itemLI

class CreateInputForm(forms.Form):
    text_input = forms.CharField(label='text-input', max_length=100)

    def save(self):
        if self.cleaned_data['text_input'] == itemLI.objects.all().latest('date').text:
            return False
        post = itemLI(text=self.cleaned_data['text_input'])
        post.save()
        return post