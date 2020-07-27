from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from shortner.views import ShortURLView

urlpatterns = [
    # url(r'^generate$', ShortURLView.as_view()),
    # url(r'^(?P<url_hash>[A-Za-z0-9]{5})$', ShortURLView.as_view()),
    path('', include('frontend.urls')),
    path('', include('shortner.urls')),

    path('admin/', admin.site.urls),

]
