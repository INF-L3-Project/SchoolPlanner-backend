from django.contrib import admin
from authentication.models import Institution


class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name','id')
    list_filters = ['name','id']


admin.site.register(Institution, InstitutionAdmin)
