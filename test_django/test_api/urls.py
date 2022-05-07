from django.urls import path
from . import views

urlpatterns = [path(
    # '',views.index,name='index'
    'create_machine/',views.Create_machine.as_view(),name='create_machine'
)]