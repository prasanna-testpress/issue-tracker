from django.contrib import admin
from .models import Issue


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "created_by",
        "assigned_to",
        "created_at",
        "status",
        "priority",
    )

    field_search = ("title",)
    list_filter = ("status", "priority")
    orderinf=('-created_at')