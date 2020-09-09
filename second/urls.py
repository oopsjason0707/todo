from  . import views
from django.urls import path, include

app_name = 'second'

urlpatterns = [   # 콤마 꼭 잊지말고...리스트, 리스트, 리스트
    path('', views.index, name='index'),
    path('favourite', views.favourite, name='favourite'),
    path('favourite_detail', views.favourite_detail, name='favourite_detail'),
    path('todo', views.todo, name='todo'),
    path('todo_detail', views.todo_detail, name='todo_detail'),
]



