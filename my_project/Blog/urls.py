from django.conf.urls import url
from .views import(
    list_view,
    post_view,
    create_view,
    update_view,
    delete_view,
    )

urlpatterns = [
    url(r'',list_view, name="blog"),
    url(r'^post/$',post_view, name="blog_post"),
    url(r'^create/$',create_view, name="blog_create"),
    url(r'^update/$',update_view, name="blog_update"),
    url(r'^delete/$',delete_view, name="blog_delete"),
    ]
