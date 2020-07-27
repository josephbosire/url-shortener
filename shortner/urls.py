"""tinyurl URL Configuration

"""
from django.urls import path
from shortner.views import ShortURLView
from django.conf.urls import url

urlpatterns = [
    url(r'^generate$', ShortURLView.as_view(),  name="generate-short-url"),
    url(r'^(?P<url_hash>[A-Za-z0-9]{5})$', ShortURLView.as_view(), name="redirect-short-url"),
]

app_name = "shortner"