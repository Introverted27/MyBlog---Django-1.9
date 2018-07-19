from django.contrib import admin
from .models import Comment

# Register your models here.
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "timestamp", "content_object", "parent", "content"]
    list_filter = ["timestamp", ]
    search_fields = ["title", "content", "content_object"]
    class Meta:
        model = Comment

admin.site.register(Comment, CommentModelAdmin)
