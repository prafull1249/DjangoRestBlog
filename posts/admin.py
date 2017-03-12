from django.contrib import admin

# Register your models here.
from posts.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','updated', 'timestamp')
    # includes fields that are displayed as hyperlinks
    list_display_links = ['updated']
    # list_filter includes fields thorugh which you can filter. A dialog appears on the side pane on right.
    list_filter = ['timestamp','updated']
    # fields which are searchable from the search bar.
    search_fields = ['title', 'content']
    # contains of fields which are editable
    list_editable = ['title']
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
