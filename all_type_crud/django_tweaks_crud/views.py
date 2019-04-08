from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .forms import CrudWithTweaksForm
from .models import CrudWithTweaks
# Create your views here.
def django_tweaks_form(request):
    data=CrudWithTweaks.objects.all()
    if request.method == 'POST':
        form=CrudWithTweaksForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Category Added Successfully')
            return HttpResponseRedirect(reverse('django_tweaks_form'))
    else:    
        form=CrudWithTweaksForm()
        action_type='Create'
    return render(request,'dashboard/django_tweaks_form.html',{'form':form,'data':data,'action_type':action_type})

def tweaks_delete(request,pk):
    data=CrudWithTweaks.objects.get(pk=pk).delete()
    messages.success(request,'Category Deleted Successfully')
    return HttpResponseRedirect(reverse('django_tweaks_form'))

def tweaks_edit(request,pk):
    data=CrudWithTweaks.objects.all()
    edit_data=CrudWithTweaks.objects.get(pk=pk)
    if request.method == 'POST':
         form=CrudWithTweaksForm(request.POST,instance=edit_data)
         if form.is_valid():
            form.save()
            messages.success(request,'Category Update Successfully')
            return HttpResponseRedirect(reverse('django_tweaks_form'))
    else:    
        form=CrudWithTweaksForm(instance=edit_data)
        action_type='Update'
    return render(request,'dashboard/django_tweaks_form.html',{'form':form,'data':data,'action_type':action_type}) 


def tweaks_status(request,pk):
    data=CrudWithTweaks.objects.get(pk=pk)
    if data.category_status == 'Active':
        data.category_status='Inactive'
        messages.info(request,'Category Status Changed Into Inactive')
    else:
        data.category_status='Active'
        messages.success(request,'Category Status Changed Into Active')
    data.save()
    return HttpResponseRedirect(reverse('django_tweaks_form'))         

