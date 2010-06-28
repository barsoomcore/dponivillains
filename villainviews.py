import simplejson as json
from django.core import serializers
from django.shortcuts import render_to_response, get_list_or_404, get_object_or_404
from django.template import RequestContext
from django.conf import settings

from dponisetting.dponivillains.models import Skill, VillainRole, VillainLevel

def villain_picker(request, villain, level='0'):

	villain_data = []
	villain_skills = []
	villain_name = villain
	if villain == 'WarLeader':
		villain = 'War Leader'
	villain_role = get_object_or_404(VillainRole, name=villain)

	villain_skills = serializers.serialize('json', villain_role.skills.all())
	villain_data = serializers.serialize('json', villain_role.levels.all())
	
		
	try:
		level = int(level)
		if 1 > level or level > 20:
			level = '0'
	except ValueError:
		level = '0'
		

	template_params = { 'villain_role': villain_role,
						'villain_data': villain_data,
						'villain_skills': villain_skills,
						'villain_level': level,
						'villain_name': villain_name
	}

	return render_to_response(
		'villain.html', 
		template_params, 
		context_instance=RequestContext(request)
	)