from django.contrib import admin
from .models import Project, Preview, Tag


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'show')


admin.site.register(Project, ProjectAdmin)


class PreviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbs', 'tag', 'project')


admin.site.register(Preview, PreviewAdmin)
admin.site.register(Tag)
