from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import home_view
from views import landing
from registration.backends.simple.views import RegistrationView

class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/notes/'


urlpatterns = patterns('',
                       # url(r'^$', home_view, name='home'),
                       url(r'^$', landing, name='home'),
                       url(r'^notes/', include('notes.urls', namespace='notes')),
                       #url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'home'}, name='logout'),
                       url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
                       url(r'^accounts/', include('registration.backends.simple.urls')),
                       url(r'^admin/', include(admin.site.urls)),
)
