
from django.urls import path

from app import views

urlpatterns = [
    path("",views.Home,name="Home"),
    path("add/",views.add,name="add"),
    path("delete/<int:id>",views.delete,name="delete"),

]