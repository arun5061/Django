from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/$', views.create_product, name="create"),
    url(r'^submit/$', views.submit_product, name="submit")
    #url(r'^class_view/$', Product_View.as_view(), name="ProductList")
    ]
