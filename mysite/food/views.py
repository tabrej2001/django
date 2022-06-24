from multiprocessing import context
import re
from django.http import HttpResponse
from django.shortcuts import redirect, render

from food.forms import ItemForm
from .models import Item
from django.template import loader


# Create your views here.

def index(request):
    '''item_list=Item.objects.all()

    template=loader.get_template('food/index.html')

    context={
      'item_list':item_list,
    }


    HttpResponse(template.render(context,request))'''
    item_list=Item.objects.all()
    context={
      'item_list':item_list,
    }
    return render(request,'food/index.html',context)


def details(request,item_id):
    #to get data belonging to particular id
    item=Item.objects.get(pk=item_id)

    context={
        'item':item,
    }

    return render(request,'food/detail.html',context)



def item(requet):
    return HttpResponse('This is item view')

def create_item(request):
  form=ItemForm(request.POST or None)

  if form.is_valid():
      form.save()
      return redirect('food:index')
  return render(request,'food/item-form.html',{'form':form}) 

def update_item(request,id):
  item=Item.objects.get(id=id)
  form=ItemForm(request.POST or None , instance=item)

  if form.is_valid():
    form.save()
    return redirect('food:index')

  return render(request,'food/item-form.html',{'form':form,'item':item})  


def item_delete(request,id):
  item=Item.objects.get(id=id)

  if request.method=='POST':
    item.delete()
    return redirect('food:index')

  return render(request,'food/item-delete.html',{'item':item})  

