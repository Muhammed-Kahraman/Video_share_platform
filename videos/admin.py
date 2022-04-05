from django.contrib import admin

from .models import Video, Comments
# Register your models here.

admin.site.register(Comments)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):

    list_display = ['title', 'author', 'created_date']

    list_display_links = ['title', 'created_date', 'author']

    search_fields = ['title']

    list_filter = ['created_date']
    class Meta:
        model = Video

