from django.contrib import admin
from .models import About, Technology, Project, Experience


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("__str__",)


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "github_link")
    search_fields = ("title",)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
