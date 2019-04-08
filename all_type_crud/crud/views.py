from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import SimpleCrud
from django.db import IntegrityError
from django.urls import reverse
# Create your views here.
def admin_login(request):
    return render(request,'login/login.html')

def dashboard(request):
    return render(request,'dashboard/home.html')  

def simple_crud(request):
    errors={}
    success={}
    value={}
    if request.method == 'POST':
        category_name=request.POST.get('category_name',None)
        category_code=request.POST.get('category_code',None)
        category_description=request.POST.get('category_description',None)
        category_status=request.POST.get('category_status',None)
        value['value']=request.POST
        if not category_name:
            errors['category_name']='Please Put Category Name'
        if not category_code:
            errors['category_code']='Please Put Category Code'
        if not category_description:
            errors['category_description']='Please Put Category Description'
        else:
            try:
                SimpleCrud.objects.create(category_name=category_name,category_code=category_code,category_description=category_description,category_status=category_status)
                value={}
                success['success']='Data Saved Successfully'
            except IntegrityError:
                errors['exist']='Already Exist'
                value={}
        return render(request,'dashboard/simple_crud.html',{'errors':errors,'success':success,'value':value})     
    else:
        context={
            'category_data':SimpleCrud.objects.all()
        }    
        return render(request,'dashboard/simple_crud.html',context)  

def delete(request,pk):
    success={}
    data=SimpleCrud.objects.get(pk=pk).delete()
    success['success']='Data Deleted Successfully'
    context={
            'category_data':SimpleCrud.objects.all(),
            'success':success
        }  
    return render(request,'dashboard/simple_crud.html',context)  
    
def status(request,pk):
    success={}
    data=SimpleCrud.objects.get(pk=pk)
    if data.category_status == 'Active':
        data.category_status ='Inactive'
        success['success']='Status Changed Into Inactive'
    else:
        data.category_status ='Active'
        success['success']='Status Changed Into Active' 
    data.save()   
    context={
            'category_data':SimpleCrud.objects.all(),
            'success':success
        }
    return render(request,'dashboard/simple_crud.html',context)            


def edit(request,pk):
    errors={}
    success={}
    if request.method == 'POST':
        category_name=request.POST.get('category_name',None)
        category_code=request.POST.get('category_code',None)
        category_description=request.POST.get('category_description',None)
        category_status=request.POST.get('category_status',None)
        if not category_name:
            errors['category_name']='Please Put Category Name'
        if not category_code:
            errors['category_code']='Please Put Category Code'
        if not category_description:
            errors['category_description']='Please Put Category Description'
        else:
            try:
                SimpleCrud.objects.filter(pk=pk).update(category_name=category_name,category_code=category_code,category_description=category_description,category_status=category_status)
                success['success']='Data Saved Successfully'
            except IntegrityError:
                errors['exist']='Already Exist'
    data=SimpleCrud.objects.get(pk=pk)    
    context={
        'data':data,
        'errors':errors,
        'success':success
    }
    return render(request,'dashboard/simple_crud_edit.html',context) 


def form_crud(request):
    return HttpResponse('form_crud')


def tweaks_crud(request):
    return HttpResponse('tweaks_crud')    