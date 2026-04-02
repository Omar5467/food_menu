from django.urls import path
from .import views

app_name='myapp'

urlpatterns = [
    path('',views.IndexClassView.as_view(), name='index'),
    path('<int:pk>/',views.FoodDetal.as_view(), name='details'),
    path('add/',views.ItemCreateView.as_view(), name='create_item'),
    path('update/<int:pk>/',views.ItemUpdateView.as_view(), name='update_item'),
    path('delete/<int:pk>/',views.ItemDeleteView.as_view(), name='delete_item'),
]