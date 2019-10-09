from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



from .models import itemLI

# Create your views here.

def index(request):
    items = itemLI.objects.order_by('id')[:]
    template = loader.get_template('index.html')
    context = {
        'items' : items,
    }
    return HttpResponse(template.render(context, request))