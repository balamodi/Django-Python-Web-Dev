from django.contrib import admin
from . models import Question, Choice
# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]
admin.site.register(Question, QuestionAdmin)

class ChoiceAdmin(admin.ModelAdmin):
	fieldsets = [
        (None,               {'fields': ['choice_text']}),
        ('Votes', {'fields': ['votes']}),
    ]
    #list_display = ('choice_text', 'votes')
admin.site.register(Choice, ChoiceAdmin)