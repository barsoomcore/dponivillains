import simplejson as json
from django.core import serializers
from django.shortcuts import render_to_response, get_list_or_404, get_object_or_404
from django.template import RequestContext
from django.conf import settings
from django.http import HttpResponse

from dponisetting.dponivillains.models import Skill, VillainRole, VillainLevel, NPC
from dponisetting import settings

def villain_picker(request, villain, level='0', name=''):

	if villain == 'WarLeader':
		villain = 'War Leader'
	
	villain_role = get_object_or_404(VillainRole, name=villain)
		
	try:
		level = int(level)
		if 1 > level or level > 20:
			level = '0'
	except ValueError:
		level = '0'
		
	template_params = { 'villain_role': villain_role,
						'villain_level': level,
						'villain_url': settings.VILLAIN_URL + villain_role.slug + '/',
	}

	return render_to_response(
		'villain_statblock.html', 
		template_params, 
		context_instance=RequestContext(request)
	)

def villain_data_json(request, villain, level='0'):

	if villain == 'WarLeader':
		villain = 'War Leader'

	villain_role = get_object_or_404(VillainRole, name=villain)
	
	return_data = '['
	return_data = return_data + serializers.serialize('json', villain_role.levels.all())
	return_data = return_data + ', ' + serializers.serialize('json', villain_role.skills.all())
	return_data = return_data + ']'
	
	return_json_data = json.dumps(return_data)
	
	return HttpResponse(
		return_data, 
		mimetype='application/json'
	)