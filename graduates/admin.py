from email.headerregistry import Group
from profile import Profile
from unittest import addModuleCleanup
from django.contrib import admin

from graduates.models import Departments, Directions, EducationForms, Faculties, Graduates, Profiles, Qualifications, Groups

admin.site.register(Faculties)
admin.site.register(Directions)
admin.site.register(Profiles)
admin.site.register(Qualifications)
admin.site.register(EducationForms)
admin.site.register(Groups)
admin.site.register(Departments)
#admin.site.register(Graduates)


@admin.register(Graduates)
class GraduatesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}