from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'date_posted', 'author')  # display fields
    list_display_links = ('title', 'date_posted', 'author') # make fields clickable
    search_fields = ['date_posted', 'author'] # search by
    list_filter = ('author',) # filter
    autocomplete_fields = ['author']