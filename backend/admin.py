from django.contrib import admin

# Register your models here.
from . import models


class QuestionAdmin(admin.ModelAdmin):
    # fields = ["published_date", "question_text"]
    list_display = ("question_text", "published_date", "was_published_recently")
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["published_date"]}),
    ]
    list_filter = ["published_date"]
    search_fields = ["question_text"]


admin.site.register(models.Choice)
admin.site.register(models.Question, QuestionAdmin)
