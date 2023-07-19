from django.contrib import admin
from django.utils.safestring import mark_safe
from wedding.models import Wedding, Comment, Photo, Moderate

admin.site.site_title = 'Админ-панель'
admin.site.site_header = 'Админ-панель'


@admin.register(Moderate)
class ModerateAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.filter(is_accepted=0)
        return queryset


@admin.register(Wedding)
class WeddingAdmin(admin.ModelAdmin):
    list_display = (Wedding.__str__, 'wedding_date', 'wedding_location')
    search_fields = ('wedding_date',)
    Wedding.__str__.short_description = 'Свадьба'



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('commenter_name', 'comment_date', 'comment_text')
    search_fields = ('commenter_name', 'comment_date')


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (Photo.__str__, 'get_html_photo', 'photo_description')
    search_fields = ('wedding',)
    fields = ('wedding', 'photo_url', 'get_html_photo', 'photo_description')
    readonly_fields = ('get_html_photo',)
    Photo.__str__.short_description = 'Свадьба'

    def get_html_photo(self, object):
        if object.photo_url:
            return mark_safe(f"<img src='{object.photo_url.url}' width=100>")

    get_html_photo.short_description = 'Фото'
