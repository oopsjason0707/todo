from  . import views
from django.urls import path, include

urlpatterns = [   # 콤마 꼭 잊지말고...리스트, 리스트, 리스트, path(url경로 text, views (함수들), 이름)
    path('', views.index, name='index'),
    path('students', views.students, name='students'),
    path('students/<int:id>', views.students_detail, name='students'),
    path('scores', views.scores, name='scores')
]


