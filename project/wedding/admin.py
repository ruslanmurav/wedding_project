from django.contrib import admin
from wedding.models import Wedding, Comment, Photo, Moderate


@admin.register(Moderate)
class ModerateAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.filter(is_accepted=0)
        return queryset


@admin.register(Wedding)
class WeddingAdmin(admin.ModelAdmin):
    list_display = (Wedding, 'wedding_date', 'wedding_location')
    search_fields = ('wedding_date',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('commenter_name', 'comment_date', 'comment_text')
    search_fields = ('commenter_name', 'comment_date')


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('photo_url', 'photo_description')
    search_fields = ('wedding',)