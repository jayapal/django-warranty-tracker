from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'warranty_tracker.views.home', name='home'),
    # url(r'^warranty_tracker/', include('warranty_tracker.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/signup/', "tracker.views.signup", name="signup"),
    url(r'', include(admin.site.urls)),
)
