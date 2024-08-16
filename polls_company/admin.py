   
from django.contrib import admin
# Register your models here.
from .models import Answer_company, Question_company, Choice_company
 
# admin.site.register(Question)
# admin.site.register(Choice)

 
 
class ChoiceInLine(admin.TabularInline):
    model = Choice_company
    extra = 3
 
 
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}), ]
    inlines = [ChoiceInLine]
 
 
admin.site.register(Question_company, QuestionAdmin)
admin.site.register(Answer_company)
