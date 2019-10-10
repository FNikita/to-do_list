from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


from .forms import CreateInputForm
from .models import itemLI

# Create your views here.

def get_input_text(request):
    if request.method == 'POST':
        form = CreateInputForm(request.POST)
        if form.is_valid():
            item = form.save()
            url = item.get_url()
            return HttpResponseRedirect(url)
    return HttpResponse("ha")



def index(request):
    items = itemLI.objects.order_by('id')[:]
    template = loader.get_template('index.html')
    context = {
        'items' : items,
    }
    return HttpResponse(template.render(context, request))