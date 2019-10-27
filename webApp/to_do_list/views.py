from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import json

from .models import ItemLi
from string import Template


def main_page(request):
    tasks = ItemLi.objects.order_by('date')
    context = {
        'items' : tasks
    }
    return render(request, "index.html", context)


@csrf_exempt
def ajax_task(request):
    if request.method == 'POST':
        if request.POST['action'] == 'add-task':
            new_text = request.POST['text']
            item = ItemLi(text=new_text)
            item.save()
            tasks = ItemLi.objects.order_by('date')
            data = {"id": item.id, "text": item.text}
            template = Template("""<li id="$id"><input class="done" type="checkbox"><span class="li-item">$text</span>                             
                        <button class="btn delete-btn"><i class="fa fa-trash trash"></i></button> 
            </li>""")
            html_li = template.substitute(id=item.id, text=item.text)           
            json_data = json.dumps(html_li)
            return HttpResponse(json_data, content_type="application/json")
        #change one task
        if request.POST['action'] == 'change_one':
            rq_id = request.POST['id']
            check_val = request.POST['chek']
            ed = ItemLi.objects.get(pk=rq_id)
            ed.check = False if check_val == 'false' else True
            ed.save()
        #change all tasks status
        elif request.POST['action'] == 'change_all':
            allItem = ItemLi.objects.all()
            check_val = request.POST['chek']
            allItem.filter(check=False).update(check=True) if check_val == 'true' else allItem.filter(check=True).update(check=False)
        elif request.POST['action'] == 'edit-task':
            id = request.POST['id']
            text_edit = request.POST['text']
            task = ItemLi.objects.get(pk=id)
            task.text = text_edit
            task.edit = True
            task.save()
        # delete task
        elif request.POST['action'] == 'del':
            id = request.POST['id']
            item = ItemLi.objects.get(pk=id)
            item.delete()
        # delete all tasks are done
        elif request.POST['action'] == 'del-all':
            items = ItemLi.objects.all()
            items.filter(check=True).delete()
    #send contant
    tasks = ItemLi.objects.order_by('date')
    context = {
        'items' : tasks
    }
    return render(request, 'index.html', context)