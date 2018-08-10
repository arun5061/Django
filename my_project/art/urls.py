from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^slog/$', views.app, name="app"),
    url(r'^submit/$', views.submit, name="submit"),
    url(r'^login/$', login, {'template_name': 'Art/login.html'}),
    #url(r'^register/$', views., {'template_name': 'Art/login.html'}),
]
