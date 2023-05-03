from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('index/',views.index),
    path('dashboard/',views.dashboard),
    path('addprod/',views.addprod),
    path('editprod/',views.editprod),
]