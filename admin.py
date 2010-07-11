from django.contrib import admin
from dponisetting.dponivillains.models import Skill, VillainRole, VillainLevel, NPC

class SkillAdmin(admin.ModelAdmin):
	list_display = ('name', 'key_ability',)

class VillainRoleAdmin(admin.ModelAdmin):
	list_display = ('name', 'description',)
	prepopulated_fields = {'slug': ('name',)}

class VillainLevelAdmin(admin.ModelAdmin):
	list_display = ('role', 'level', 'base_combat_bonus', 'abilities',)
	list_filter = ('role',)
	ordering = ('role', 'level',)
	
class NPCAdmin(admin.ModelAdmin):
	list_display = ('name', 'role_level',)
	prepopulated_fields = {'slug': ('name', 'role_level',)}

admin.site.register(Skill, SkillAdmin)
admin.site.register(VillainRole, VillainRoleAdmin)
admin.site.register(VillainLevel, VillainLevelAdmin)
admin.site.register(NPC, NPCAdmin)