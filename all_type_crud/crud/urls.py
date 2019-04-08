from django.urls import path
from . import views
urlpatterns = [
    path('',views.admin_login,name='admin_login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('dashboard/simple_crud',views.simple_crud,name='simple_crud'),
    path('dashboard/simple_crud/simple_delete/<int:pk>',views.delete,name='simple_delete'),
    path('dashboard/simple_crud/simple_status/<int:pk>',views.status,name='simple_status'),
    path('dashboard/simple_crud/simple_edit/<int:pk>',views.edit,name='simple_edit'),
    path('dashboard/form_crud',views.form_crud,name='form_crud'),
    path('dashboard/tweaks_crud',views.tweaks_crud,name='tweaks_crud'),
]