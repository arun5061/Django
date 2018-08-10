from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/$', views.todo_list, name="list"),
    url(r'^add/$', views.addTodo, name="add"),
    url(r'^complete/(?P<pk>\d+)/$', views.completeTodo, name="complete"),
    url(r'^delcomplete/$', views.deleteComplete, name="delcomplete"),
    url(r'^delall/$', views.deleteAll, name="delall"),
]
