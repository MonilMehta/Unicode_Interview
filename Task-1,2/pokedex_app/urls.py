from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('search/',views.search,name="search"),
    path('caught/', views.caught, name='caught'),
    path('list/', views.list, name='list'),
]