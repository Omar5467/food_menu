from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import item
from myapp.forms import ItemForm

# Create your views here.
def index(request):
    item_list = item.objects.all()
    context={
        'item_list': item_list
    }
    return render(request,'myapp/index.html',context)



def details(request,id):
    item_detail = item.objects.get(id=id)
    context = {
        'item_detail' : item_detail
    }
    return render(request,'myapp/details.html',context)



def create_item(request):
    form = ItemForm(request.POST or None)
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:index')

        # print('Form is a post method')
        # print(request.POST)
    
    context = {
        'form':form
    }
    return render(request,'myapp/item-form.html',context)


def update_item(request,id):
    items=item.objects.get(id=id)
    form = ItemForm(request.POST or None,instance=items)
    if form.is_valid():
        form.save()
        return redirect('myapp:index')
    context={
        'form':form
    }
    
    return render(request,'myapp/item-form.html',context)

def delete_item(request,id):
    items=item.objects.get(id=id)
    if request.method=="POST":
        items.delete()
        return redirect('myapp:index')

    return render(request,'myapp/delete_item.html')