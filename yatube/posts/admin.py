from django.contrib import admin

from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    """Класс описывающий таблицу Post"""
    list_display = ("pk", "text", "pub_date", "author", "group")
    search_fields = ("text",)
    list_filter = ("pub_date",)
    list_editable = ('group',)
    empty_value_display = "-пусто-"


class GroupAdmin(admin.ModelAdmin):
    """Класс описывающий таблицу Group"""
    list_display = ("title", "slug", "description")
    search_fields = ("title",)
    empty_value_display = "-пусто-"


admin.site.register(Group, GroupAdmin)
admin.site.register(Post, PostAdmin)
