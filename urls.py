from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'main.views.index'),
)

# Serve static content through Django.
# (This way is less efficient than having the web server do it and unless 
# there is a decent caching layer, SERVE_STATIC should be False for production)
from django.conf import settings
if settings.SERVE_STATIC:
	urlpatterns += patterns('',
	    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
	    	'document_root': settings.MEDIA_ROOT }),
	)
