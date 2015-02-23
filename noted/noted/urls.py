from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import home_view


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'noted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', home_view, name='home'),
    url(r'^notes/', include('notes.urls', namespace='notes')),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'home'}, name='logout'),
    #url(r'^admin/', include(admin.site.urls)),
)
