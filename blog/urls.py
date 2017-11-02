from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accueil$', views.home, name='home'),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^importateur/list', views.importateur_list, name='importateur_list'),
    url(r'^importateur/(?P<pk>[0-9]+)/$', views.importateur_detail, name='importateur_detail'),

    url(r'^importateur/new/$', views.importateur_new, name='importateur_new'),

    url(r'^importateur/(?P<pk>[0-9]+)/edit/$', views.importateur_edit, name='importateur_edit'),
    #url(r'^author/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author_delete')

]