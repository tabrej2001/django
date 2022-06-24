from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from . import views

#Namespacing
app_name='food'

urlpatterns = [
    path('', views.index,name='index'),
    path('item/',views.item,name='item'),
    path('<int:item_id>/',views.details,name='details'),
    #Add item
    path('add',views.create_item,name='create_item'),
    path('update/<int:id>/',views.update_item,name='update_item'),
    #delete
    path('delete/<int:id>/',views.item_delete,name='item_delete'),
    



]
