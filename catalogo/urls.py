from django.conf.urls import url
from catalogo.views import *

urlpatterns = [
    url(r'^$', lista_produtos, name='lista_produtos'),
    url(r'^(?P<slug>[\w_-]+)/$', categoria, name='categoria'),
    url(r'^produtos/(?P<slug>[\w_-]+)/$', produto, name='produto'),
]