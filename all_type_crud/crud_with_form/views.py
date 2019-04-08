from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .forms import CrudForm
from .models import CrudWithForm
from django.contrib import messages
# Create your views here.
def django_form(request):
    data=CrudWithForm.objects.all()
    if request.method == 'POST':
        form=CrudForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Category Added Successfully')
            return HttpResponseRedirect(reverse('django_form'))
    else:    
        form=CrudForm()
        action_type='Create'
    return render(request,'dashboard/crud_with_django_form.html',{'form':form,'data':data,'action_type':action_type})

def status(request,pk):
    data=CrudWithForm.objects.get(pk=pk)
    if data.category_status == 'Active':
        data.category_status='Inactive'
        messages.info(request,'Category Status Changed Into Inactive')
    else:
        data.category_status='Active'
        messages.success(request,'Category Status Changed Into Active')
    data.save()
    return HttpResponseRedirect(reverse('django_form'))

def edit(request,pk):
     data=CrudWithForm.objects.all()
     edit_data=CrudWithForm.objects.get(pk=pk)
     if request.method == 'POST':
         form=CrudForm(request.POST,instance=edit_data)
         if form.is_valid():
            form.save()
            messages.success(request,'Category Added Successfully')
            return HttpResponseRedirect(reverse('django_form'))
     else:    
        form=CrudForm(instance=edit_data)
        action_type='Update'
     return render(request,'dashboard/crud_with_django_form.html',{'form':form,'data':data,'action_type':action_type})   

def delete(request,pk):
    data=CrudWithForm.objects.get(pk=pk).delete()
    messages.info(request,'Category Deleted Successfully')
    return HttpResponseRedirect(reverse('django_form'))