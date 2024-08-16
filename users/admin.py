from django.contrib import admin

from users.models import UserCompany, UserGraduate, UserTeacher

# admin.site.register(User)
    
@admin.register(UserGraduate, UserCompany, UserTeacher)
class UserAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('username',)}
    