from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


from .forms import CreateInputForm, CreatDeletForm
from .models import itemLI

def get_input_text(request):
    if request.method == 'POST':
        form = CreateInputForm(request.POST)
        if form.is_valid():
            item = form.save()
            item.save()
            return HttpResponse(index(request))
    return HttpResponse(index(request))

def delet_item(request):
    if request.method == 'POST':
        form = CreatDeletForm(request.POST)
        if form.delete_li():
            return HttpResponse(index(request))
    return HttpResponse(index(request))

def index(request):
    items = itemLI.objects.order_by('id')[:]
    template = loader.get_template('index.html')
    context = {
        'items' : items,
    }
    return HttpResponse(template.render(context, request))


def ajax_request(request):
    if request.method == 'GET':
        return HttpResponse("olala")