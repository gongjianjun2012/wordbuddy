from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WordBuddy.views.home', name='home'),
    # url(r'^WordBuddy/', include('WordBuddy.foo.urls')),
    (r'^js/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'D:/google/WordBuddy/siteResources/js'}
     ),

    (r'^css/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'D:/google/WordBuddy/siteResources/css/'}
     ),

    (r'^image/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'D:/google/WordBuddy/siteResources/image/'}
     ),

    (r'^$', 'Demo.views.Demo_index'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
