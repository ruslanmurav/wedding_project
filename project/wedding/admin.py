from django.contrib import admin

from wedding.models import Wedding, Comment, Photo, Moderate


admin.site.register(Wedding)
admin.site.register(Comment)
admin.site.register(Photo)


@admin.register(Moderate)
class ModerateAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.filter(is_accepted=0)
        return queryset
