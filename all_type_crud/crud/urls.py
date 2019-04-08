from django.urls import path
from . import views
urlpatterns = [
    path('',views.admin_login,name='admin_login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('dashboard/simple_crud',views.simple_crud,name='simple_crud'),
    path('dashboard/simple_crud/delete/<int:pk>',views.delete,name='delete'),
    path('dashboard/simple_crud/status/<int:pk>',views.status,name='status'),
    path('dashboard/simple_crud/edit/<int:pk>',views.edit,name='edit'),
    path('dashboard/form_crud',views.form_crud,name='form_crud'),
    path('dashboard/tweaks_crud',views.tweaks_crud,name='tweaks_crud'),
]