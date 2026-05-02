from django.urls import path
from .import views
# from django.views.decorators.cache import cache_page # Import the cache_page decorator

app_name='myapp'

urlpatterns = [
    #URL patterns of the API
    path('items-json/', views.item_list_json, name='item_list_json'),
    #URL pattern for API using Django REST Framework
    path('items-api/', views.item_list_api, name='item_list_api'),


    #URL patterns of the Django app
    path('',views.index, name='index'),
    # path('', cache_page(60 * 15)(views.index), name='index'),# Cache the index view for 15 minutes url cache
    path('<int:id>/',views.details, name='details'),
    path('add/',views.create_item, name='create_item'),
    path('update/<int:pk>/',views.ItemUpdateView.as_view(), name='update_item'),
    path('delete/<int:pk>/',views.ItemDeleteView.as_view(), name='delete_item'),
]