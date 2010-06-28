from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^$', 
    	'django.views.generic.simple.direct_to_template', 
    	{'template': 'villain_intro.html'}, 
    	name='villain_intro'
    )
)

urlpatterns += patterns('dponisetting.dponivillains.villainviews',
    url(r'^(?P<villain>[-\w]+)/$', 'villain_picker', name='villain_name'),
    url(r'^(?P<villain>[-\w]+)/(?P<level>[-\w]+)$',  'villain_picker', name='villain_name_and_level'),
)