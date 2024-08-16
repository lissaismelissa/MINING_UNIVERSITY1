   
from django.contrib import admin
# Register your models here.
from .models import Answer, Question, Choice
 
# admin.site.register(Question)
# admin.site.register(Choice)

 
 
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3
 
 
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}), ]
    inlines = [ChoiceInLine]
 
 
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)