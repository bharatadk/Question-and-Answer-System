from django.contrib import admin
from .models import *

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')
    search_fields = ('title','user')
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Comment)
admin.site.register(Upvote)
admin.site.register(Downvote)