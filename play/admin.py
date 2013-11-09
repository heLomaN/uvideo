from play.models import Paper,Question
from django.contrib import admin

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 30

class PaperAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['paper','which_state','year']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [QuestionInline]

admin.site.register(Paper, PaperAdmin)

#admin.site.register(Paper)
#admin.site.register(Question)