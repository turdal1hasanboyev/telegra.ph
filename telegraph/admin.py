from django.contrib import admin

from .models import Post


admin.site.site_header = "telegra.ph Admin Panel"
admin.site.site_title = "telegra.ph Admin Panel"
admin.site.index_title = "Welcome to telegra.ph Admin Panel!"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Admin panel for Post model.
    """

    ordering = ['-created_at']
    list_display = (
        'id',
        'title',
        'author',
        'created_at',
        'updated_at',
    )
    search_fields = ('title',)
