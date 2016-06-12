from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="light/index.html"), name="index"),
    url(r'^list$', LightListView.as_view(template_name="light/light_list.html"), name="light-list"),
    url(r'^list2$', LightListView.as_view(template_name="light/light_list_json.html"), name="light-list2"),
    url(r'create$', LightCreateView.as_view(), name="light-create"),
    url(r'(?P<pk>[0-9]+)/update$', LightUpdateView.as_view(), name="light-update"),


    url(r'^list/json$', LightJSONListView.as_view(), name="light-json-list"),
    url(r'create/json$', LightJSONCreateView.as_view(), name="light-json-create"),
    url(r'(?P<pk>[0-9]+)/update/json$', LightJSONUpdateView.as_view(), name="light-json-update"),
]
