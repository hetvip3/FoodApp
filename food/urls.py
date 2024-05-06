from django.urls import path
from . views import *


app_name = 'food'

urlpatterns = [
    #/food/
    path('',index, name='index'),
    #/food/1
    path('food/<int:item_id>/',detail , name='detail'),

    path('add',create_item)
]