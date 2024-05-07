from django.urls import path
from . views import *


app_name = 'food'

urlpatterns = [
    #/food/
    path('',index, name='index'),
    #/food/1
    path('food/<int:item_id>/',detail , name='detail'),
    #add
    path('add',create_item,name='create_item'),
    #edit
    path('update/<int:id>',update_item,name='update_item'),
    #delete
    path('delete/<int:id>',delete_item,name='delete_item')
]