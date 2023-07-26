from django.contrib import admin
from django.utils.safestring import mark_safe

import project.settings
from wedding.models import Wedding, Comment, Photo, Moderate, SitePhotos, File, Video, Text

admin.site.site_title = 'Админ-панель'
admin.site.site_header = 'Админ-панель'


# @admin.register(File)
# class FileAdmin(admin.ModelAdmin):
#     list_display = ('file', 'mark')





@admin.register(SitePhotos)
class SitePhotosAdmin(admin.ModelAdmin):
    list_display = ('get_html_photo',)
    fields = ('site_photo', 'get_html_photo', 'photo_name' if project.settings.DEBUG else None)
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
        if object.commenter_avatar:
            return mark_safe(f"<img src='{object.commenter_avatar.url}' width=100>")

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


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = (Video.__str__,)
    fields = ('wedding', 'file', 'get_html_photo')
    readonly_fields = ('get_html_photo',)
    Video.__str__.short_description = 'Видео'

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.filter(mark=1)
        return queryset

    def get_html_photo(self, object):
        if object.file:
            return mark_safe(f'<video width="400" height="300" controls="controls"> <source src="{ object.file.url }" type="video/mp4; codecs=\"avc1.42E01E, mp4a.40.2\""></video>')

    get_html_photo.short_description = 'Видео'


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ('file_name',)
    fields = ('file_name', 'file', 'mark')
    readonly_fields = ('file_name', 'mark')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.filter(mark=2)
        return queryset
