from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import item
from myapp.forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
import logging
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.http import JsonResponse
from .serializers import ItemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response



logger = logging.getLogger(__name__)



@api_view(['GET'])
def item_list_api(request):
    items = item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)







#API WITH JSON RESPONSE without using Django REST Framework
def item_list_json(request):
    items = item.objects.all().values('id', 'item_name', 'item_price', 'item_desc')
    print(items)
    return JsonResponse(list(items), safe=False)







# Create your views here.
# @login_required
# @cache_page(60 * 15)  # Cache for 15 minutes
# @vary_on_headers('User-Agent')  # Vary cache based on User-Agent header 
def index(request):
    logger.info("fetching all items from the database")
    logger.info(f"Time [{timezone.now().isoformat()}] User {request.user} requested item list from {request.META.get('REMOTE_ADDR')}")
    item_list = item.objects.all()
    logger.debug(f"Number of items fetched: {item_list.count()}")

    paginator = Paginator(item_list, 5) # Show 5 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context={
        'page_obj': page_obj
    }
    return render(request,'myapp/index.html',context)


# class IndexClassView(ListView):
#     model = item
#     template_name = 'myapp/index.html'
#     context_object_name = 'item_list'



def details(request,id):
    logger.info(f"Fetching item with id: {id}")
    try:
        item_detail = get_object_or_404(item, pk=id)
        logger.debug(f"Item fetched: {item_detail.item_name} (${item_detail.item_price})")
    except Exception as e:
        logger.error(f"Error fetching item with id %s: %s", id,e)
        # return HttpResponse("Item not found", status=404)
    context = {
        'item_detail' : item_detail
    }
    return render(request,'myapp/details.html',context)


# class FoodDetal(DetailView):
#     model = item
#     template_name = 'myapp/details.html'
#     context_object_name = 'item_detail'


def create_item(request):
    form = ItemForm(request.POST or None)
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.instance.user_name = request.user
            form.save()
            return redirect('myapp:index')
        else:
            print(form.errors['item_price'])
        # print('Form is a post method')
        # print(request.POST)
    
    context = {
        'form':form
    }
    return render(request,'myapp/item-form.html',context)


# class ItemCreateView(CreateView):
#     model = item
#     fields=['item_name','item_desc','item_price','item_image']
    
#     def form_valid(self, form):
#         form.instance.user_name = self.request.user
#         return super().form_valid(form)


# def update_item(request,id):
#     items=item.objects.get(id=id)
#     form = ItemForm(request.POST or None,instance=items)
#     if form.is_valid():
#         form.save()
#         return redirect('myapp:index')
#     context={
#         'form':form
#     }
    
#     return render(request,'myapp/item-form.html',context)


class ItemUpdateView(UpdateView):
    model = item
    fields = ['item_name','item_desc','item_price','item_image']
    template_name_suffix = '_update_form'

    # prevent users to edit other users items
    def get_queryset(self):
        return item.objects.filter(user_name=self.request.user)
            
    

# def delete_item(request,id):
#     items=item.objects.get(id=id)
#     if request.method=="POST":
#         items.delete()
#         return redirect('myapp:index')

#     return render(request,'myapp/delete_item.html')


class ItemDeleteView(DeleteView):
    model = item
    success_url = reverse_lazy('myapp:index')
    # template_name_suffix ='_delete'

def get_object(request):
    for items in item.objects.all():
        print(items.item_name)

def get_objects_optimized(request):
    items = item.objects.only('item_name')
    for item in items:
        print(item.item_name)