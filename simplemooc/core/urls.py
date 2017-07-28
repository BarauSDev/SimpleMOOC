from django.conf.urls import url,patterns, include

from simplemooc.core.views import home, contact

urlpatterns = patterns('', 
    url(r'^$', home, name='home'),
    url(r'^contato/$', contact, name='contact'),
)