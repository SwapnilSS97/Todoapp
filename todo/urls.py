from django.urls import path
from todo import views
urlpatterns = [
    path('',views.index,name='index'),
    path('deleteTask/<int:pk>',views.deleteTask,name='deleteTask')
]
