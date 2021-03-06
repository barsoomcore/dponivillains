from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^$', 
    	'django.views.generic.simple.direct_to_template', 
    	{'template': 'villain_intro.html', 'extra_context':{'villain_role': 'Introduction'}}, 
    	name='villain_intro'
    )
)

urlpatterns += patterns('dponisetting.dponivillains.villainviews',
    url(r'^(?P<villain>[-\w]+)/$', 'villain_picker', name='villain_role'),
    url(r'^(?P<villain>[-\w]+)/(?P<level>[-\w]+)$',  'villain_picker', name='villain_role_and_level'),
)