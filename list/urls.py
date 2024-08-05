from django.urls import path, re_path

from list import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^delete/(?P<id>\d+)/$', views.delete_task, name='task_delete')
]

