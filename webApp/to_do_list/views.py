from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


from .templates.forms import CreateInputForm
from .models import itemLI

# Create your views here.

def get_input_text(request):
    if request.method == 'POST':
        text = request.POST['text-task']
        if text:
            q = itemLI(len(itemLI.objects.order_by('id')[:])+1, False, text)
            print(q)
            q.save()
            items = itemLI.objects.order_by('id')[:]
            template = loader.get_template('index.html')
            context = {
                'items' : items,
            }
            return HttpResponse(template.render(context, request))
    return HttpResponse("a")



def index(request):
    items = itemLI.objects.order_by('id')[:]
    template = loader.get_template('index.html')
    context = {
        'items' : items,
    }
    return HttpResponse(template.render(context, request))