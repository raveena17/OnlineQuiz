from django.contrib import admin

from .models import Attendee, Question, Choice, Result

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
	model = Choice
	#extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['subject']}),
        (None,               {'fields': ['question_text']}),
        (None,               {'fields': ['answer_text']}),
        ('Date information', {'fields': ['pub_date']}),
        # 	'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']          #filter box in right bottom
    search_fields = ['question_text']   #search box

admin.site.register(Attendee)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Result)
