from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import json

from .models import itemLI


@csrf_exempt
def main_page(request):
    tasks = itemLI.objects.order_by('date')
    context = {
        'items' : tasks
    }
    return render(request, "index.html", context)


@csrf_exempt
def ajax_task(request, **kwargs):
    if request.method == 'GET':
        if request.GET['action'] == 'add-task':
            new_text = request.GET['text']
            item = itemLI(text=new_text)
            item.save()
            tasks = itemLI.objects.order_by('date')
            data = {"id": item.id, "text": item.text}
            json_data = json.dumps(data)
            return HttpResponse(json_data, content_type="application/json")
        #change one task
    if request.method == 'POST':
        if request.POST['action'] == 'change_one':
            rq_id = request.POST['id']
            check_val = request.POST['chek']
            ed = itemLI.objects.get(pk=rq_id)
            ed.check = False if check_val == 'false' else True
            ed.save()
        #change all tasks status
        elif request.POST['action'] == 'change_all':
            allItem = itemLI.objects.all()
            check_val = request.POST['chek']
            if check_val == 'true':
                allItem.filter(check=False).update(check=True)
            else:
                allItem.filter(check=True).update(check=False) 
        elif request.POST['action'] == 'edit-task':
            id = request.POST['id']
            text_edit = request.POST['text']
            task = itemLI.objects.get(pk=id)
            task.text = text_edit
            task.edit = True
            task.save()
        # delete task
        elif request.POST['action'] == 'del':
            id = request.POST['id']
            item = itemLI.objects.get(pk=id)
            item.delete()
        # delete all tasks are done
        elif request.POST['action'] == 'del-all':
            items = itemLI.objects.all()
            items.filter(check=True).delete()

    #send contant
    tasks = itemLI.objects.order_by('date')
    context = {
        'items' : tasks
    }
    return render(request, 'index.html', context)