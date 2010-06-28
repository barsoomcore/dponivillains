from django.contrib import admin
from dponisetting.dponivillains.models import Skill, VillainRole, VillainLevel

class SkillAdmin(admin.ModelAdmin):
	list_display = ('name', 'key_ability',)

class VillainRoleAdmin(admin.ModelAdmin):
	list_display = ('name', 'description',)

class VillainLevelAdmin(admin.ModelAdmin):
	list_display = ('role', 'level', 'base_combat_bonus', 'abilities',)
	list_filter = ('role',)
	ordering = ('role', 'level',)

admin.site.register(Skill, SkillAdmin)
admin.site.register(VillainRole, VillainRoleAdmin)
admin.site.register(VillainLevel, VillainLevelAdmin)