from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codeBash.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'google.views.home'),
	url(r'^about/$', 'google.views.about'),
	url(r'^contact/$', 'google.views.contact'),
	url(r'^reports/$', 'google.views.reports'),
	url(r'^analytics/$', 'google.views.analytics'),
	url(r'^export/$', 'google.views.export'),
	url(r'^pageViews/$', 'google.views.pageViews'),
	url(r'^demogra/$', 'google.views.demogra'),
	url(r'^settings/$', 'google.views.settings'),
	url(r'^help/$', 'google.views.help'),

)
