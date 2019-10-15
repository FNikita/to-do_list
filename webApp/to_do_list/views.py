from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


from .forms import CreateInputForm
from .models import itemLI


def main_page(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        form = CreateInputForm(request.POST)
        if form.is_valid():
            item = form.save()
    tasks = itemLI.objects.order_by('date')
    context = {
        'items' : tasks
    }
    return render(request, "index.html", context)


@csrf_exempt
def ajax_task(request):
    if request.method == 'POST':
        #change one task
        if request.POST['action'] == 'change_one':
            rq_id = request.POST['id']
            check_val = request.POST['chek']
            ed = itemLI.objects.get(pk=rq_id)
            if check_val == 'false':
                ed.check = False
            else:
                ed.check = True
            ed.save()
        #change all tasks status
        elif request.POST['action'] == 'change_all':
            allItem = itemLI.objects.all()
            check_val = request.POST['chek']
            # need optimizate
            if check_val == 'true':
                allItem.filter(check=False).update(check=True)
            else:
                allItem.filter(check=True).update(check=False)
            #for item in allItem:
            #    item.check =  True if check_val == 'true' else False
            #    item.save()
        #edit text task 
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
            #need optimize
            items.filter(check=True).delete()
            #for item in items:
            #    if item.check:
            #        item.delete()
    #send contant
    tasks = itemLI.objects.order_by('date')
    context = {
        'items' : tasks
    }
    return render(request, 'index.html', context)