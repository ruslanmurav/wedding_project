from django.contrib import admin
from django.utils.safestring import mark_safe
from wedding.models import Wedding, Comment, Photo, Moderate, SitePhotos

admin.site.site_title = 'Админ-панель'
admin.site.site_header = 'Админ-панель'


@admin.register(SitePhotos)
class SitePhotosAdmin(admin.ModelAdmin):
    list_display = ('get_html_photo',)
    fields = ('site_photo', 'get_html_photo')
    readonly_fields = ('get_html_photo',)

    def get_html_photo(self, object):
        if object.site_photo:
            return mark_safe(f"<img src='{object.site_photo.url}' width=100>")

    get_html_photo.short_description = 'Фото'



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
    fields = ('commenter_name', 'commenter_avatar', 'get_html_photo', 'comment_text', 'comment_date', 'is_accepted')
    readonly_fields = ('get_html_photo',)

    def get_html_photo(self, object):
        if object.site_photo:
            return mark_safe(f"<img src='{object.site_photo.url}' width=100>")

    get_html_photo.short_description = 'Фото'


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
