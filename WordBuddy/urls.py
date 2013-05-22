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
         # before deployment, need be modified.
    (r'^css/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'D:/google/WordBuddy/siteResources/css/'}
     ),

    (r'^image/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'D:/google/WordBuddy/siteResources/image/'}
     ),

    url(r'^$', 'Demo.views.Demo_index',name="Demo_index"),
    url(r'^SearchWordAndPhrase/$','Demo.views.SearchWordAndPhrase'),
    url(r'^SearchWordLists/(\d{1,6})/$','Demo.views.SearchWordLists'),
    url(r'^SearchWordRoots/(\d{1,6})/$','Demo.views.SearchWordRoots'),
    url(r'^SearchBasicPhoneme/(\d{1,6})/$','Demo.views.SearchBasicPhoneme'),
    url(r'^LetterGroup/$','Demo.views.LetterGroup'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
