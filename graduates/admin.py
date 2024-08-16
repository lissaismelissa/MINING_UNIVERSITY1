from email.headerregistry import Group
from profile import Profile
from unittest import addModuleCleanup
from django.contrib import admin

from graduates.models import Departments, Directions, EducationForms, Faculties, Graduates, Profiles, Qualifications, Groups, Companies, Statuses
from users.models import Comments

admin.site.register(Faculties)
admin.site.register(Directions)
admin.site.register(Profiles)
admin.site.register(Qualifications)
admin.site.register(EducationForms)
admin.site.register(Groups)
admin.site.register(Departments)
admin.site.register(Comments)
admin.site.register(Companies)
admin.site.register(Statuses)


@admin.register(Graduates)
class GraduatesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}