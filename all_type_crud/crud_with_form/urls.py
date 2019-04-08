from django.urls import path
from . import views
urlpatterns = [
    path('',views.django_form,name='django_form'),
    path('status/<int:pk>',views.status,name='status'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('/edit/<int:pk>',views.edit,name='edit'),
]