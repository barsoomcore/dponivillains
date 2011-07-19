from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.conf import settings

from dponisetting.dponivillains.models import VillainRole
from dponisetting import settings

def villain_picker(request, villain, level='0'):

	villain_role = get_object_or_404(VillainRole, slug=villain)
		
	try:
		level = int(level)
		if 1 > level or level > 20:
			level = '0'
	except ValueError:
		level = '0'
		
	template_params = { 'villain_role': villain_role,
						'villain_level': level,
	}

	return render_to_response(
		'villain_statblock.html', 
		template_params, 
		context_instance=RequestContext(request)
	)