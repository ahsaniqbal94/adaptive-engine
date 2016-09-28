from django.contrib import admin

# Register your models here.
from .models import *
from lti.models import *

def get_generic_label(obj):
	return "{}: {}".format(obj._meta.model_name, obj.pk)

class ActivityAdmin(admin.ModelAdmin):
	list_display = ['name','pk', 'module','usage_id']

class SequenceItemAdmin(admin.ModelAdmin):
	list_display = ['get_label','activity','get_module','get_user','get_username','position']
	list_filter = ['user_module']

	def get_user(self, obj):
		return obj.user_module.user.pk
	get_user.short_description = 'user'
	get_user.admin_order_field = 'user_module__user'

	def get_username(self, obj):
		return obj.user_module.ltiparameters.lis_person_sourcedid
	get_username.short_description = 'edx username'
	get_username.admin_order_field = 'user_module__ltiparameters__lis_person_sourcedid'

	def get_module(self, obj):
		return obj.user_module.module.pk
	get_module.short_description = 'module'
	get_module.admin_order_field = 'user_module__module'

	def get_label(self,obj):
		return get_generic_label(obj)

class LtiParametersAdmin(admin.ModelAdmin):
	list_display = ['get_label','user_module', 'get_module', 'get_user', 'lis_person_sourcedid', 'timestamp_last_launch']
	readonly_fields = ['timestamp_last_launch']

	def get_module(self, obj):
		return obj.user_module.module.pk
	get_module.short_description = 'module'
	get_module.admin_order_field = 'user_module__module'

	def get_user(self, obj):
		return obj.user_module.user.pk
	get_user.short_description = 'user'
	get_user.admin_order_field = 'user_module__user'

	def get_label(self,obj):
		return get_generic_label(obj)

class AttemptAdmin(admin.ModelAdmin):
	list_display = ['get_label','activity','username', 'points','max_points','sequence_item','user','timestamp']
	readonly_fields = ['timestamp']
	def get_label(self,obj):
		return get_generic_label(obj)

class UserModuleAdmin(admin.ModelAdmin):
	list_display = ['get_label','user','module','grade','last_position']
	def get_label(self,obj):
		return get_generic_label(obj)

admin.site.register(Module)
admin.site.register(Activity, ActivityAdmin)
# admin.site.register(Problem)
# admin.site.register(Answer)
# admin.site.register(Event)
admin.site.register(Attempt, AttemptAdmin)
admin.site.register(SequenceItem, SequenceItemAdmin)
admin.site.register(LtiParameters, LtiParametersAdmin)
admin.site.register(UserModule, UserModuleAdmin)