from django.conf.urls import include, url
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^contacts/client/new$', views.client_new, name='client_new'),
    url(r'^contacts/client/(?P<pk>[0-9]+)/edit/$', views.client_edit, name='client_edit'),
    url(r'^contacts/client/(?P<pk>[0-9]+)/$', views.client_detail, name='client_detail'),
    url(r'^contacts/client/list$', views.client_list, name='client_list'),

]

if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


