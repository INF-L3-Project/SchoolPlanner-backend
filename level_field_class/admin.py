from django.contrib import admin
from level_field_class.models import Grade, Field, Group, Level


class GradeAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'level', 'field')
    list_search = ('name',)
    list_filter = ('level__name', 'field__name')


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'grade')
    list_search = ('name',)
    list_filter = ('grade__name',)


admin.site.register(Field)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Level)
admin.site.register(Group, GroupAdmin)