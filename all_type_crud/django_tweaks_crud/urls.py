from django.urls import path
from . import views
urlpatterns = [
    path('',views.django_tweaks_form,name='django_tweaks_form'),
    path('tweaks_delete/<int:pk>',views.tweaks_delete,name='tweaks_delete'),
    path('tweaks_edit/<int:pk>',views.tweaks_edit,name='tweaks_edit'),
    path('tweaks_status/<int:pk>',views.tweaks_status,name='tweaks_status')
]