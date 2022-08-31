from django.urls import path
from app1.views import creates, lists, deletes, edits, details

urlpatterns = [
    
    path('', creates, name='creates'),
    path('list/', lists, name='lists'),
    path('delete/<pk>/', deletes, name='deletes'),
    path('edit/<pk>/', edits, name='edits'),
    path('detail/<pk>/',details,name='details')

]
