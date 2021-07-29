from django.urls import path
from myapp import views
app_name='myapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('pers/',views.index1,name='index1'),
    path('list1/',views.list1,name='list1'),
    path('addpers/',views.addpers,name='addpers'),
    path('listpage/',views.listpage,name='listpage'),
    path('listpage1/',views.listpage1,name='listpage1'),
    path('editpers/<int:pk>/',views.editpers,name='editpers'),
]
