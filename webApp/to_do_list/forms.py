from django import forms

from .models import itemLI

class CreateInputForm(forms.Form):
    text_input = forms.CharField(label='text-input', max_length=100)

    def save(self):
        post = itemLI(len(itemLI.objects.order_by('id')[:])+1, False, self.cleaned_data['text_input'])
        return post

class CreatDeletForm(forms.Form):
    delete_item = forms.BooleanField(label='delete-item')

    def delete_li(self):
        deleted_item = itemLI.objects.order_by('id')[0]
        if deleted_item.delete()[0] == 1:
            return True
        return False