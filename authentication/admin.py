from django.contrib import admin
from authentication.models import Institution


class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Institution, InstitutionAdmin)
