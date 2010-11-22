from django.core import serializers
from django.db import models

class Skill(models.Model):
	ABILITY_CHOICES = (
		('Strength', 'Strength'),
		('Dexterity', 'Dexterity'),
		('Constitution', 'Constitution'),
		('Intelligence', 'Intelligence'),
		('Wisdom', 'Wisdom'),
		('Charisma', 'Charisma'),
	)
		
	name = models.CharField(max_length=100, primary_key=True)
	key_ability = models.CharField(max_length=20, choices=ABILITY_CHOICES)
	
	def __unicode__(self):
		return u'%s' % (self.name)
	
	def get_by_natural_key(self, name):
		return self.get(name=name)

class VillainRole(models.Model):
	name = models.CharField(max_length=100, primary_key=True)
	skills = models.ManyToManyField(Skill, related_name='roles')
	description = models.TextField()
	slug = models.SlugField(max_length=100, unique=True)
	
	def __unicode__(self):
		return u'%s' % (self.name)
	
	@models.permalink
	def get_absolute_url(self):
		return('villain_role', (), { 'villain': self.name })
	
	def as_json(self):
		json_data = '['
		json_data = json_data + serializers.serialize('json', self.levels.all())
		json_data = json_data + ', ' + serializers.serialize('json', self.skills.all())
		json_data = json_data + ']'
		return json_data

class VillainLevel(models.Model):
	role = models.ForeignKey(VillainRole, to_field = 'name', related_name='levels')
	level = models.IntegerField()
	base_combat_bonus = models.IntegerField()
	secondary_combat_bonus = models.IntegerField(blank=True, null=True)
	fortitude = models.IntegerField()
	reflex = models.IntegerField()
	will = models.IntegerField()
	abilities = models.TextField(blank=True)
	dc = models.IntegerField(blank=True, null=True)
	damage = models.IntegerField()
	toughness = models.IntegerField()
	strength = models.IntegerField()
	dexterity = models.IntegerField()
	constitution = models.IntegerField()
	intelligence = models.IntegerField()
	wisdom = models.IntegerField()
	charisma = models.IntegerField()
	
	def __unicode__(self):
		return u'%s %s' % (self.role, self.level)
	
	class Meta:
		unique_together = ('role', 'level')
	
	@models.permalink
	def get_absolute_url(self):
		return('villain_role_and_level', { 'villain': self.role, 'level': self.level })
	

class NPC(models.Model):
	role_level = models.ForeignKey(VillainLevel)
	name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)
	
	def __unicode__(self):
		return u'%s' % (self.name)
	
	@models.permalink
	def get_absolute_url(self):
		return('npc', (), {'villain': self.role_level.role, 'level': self.role_level.level, 'name': self.slug})