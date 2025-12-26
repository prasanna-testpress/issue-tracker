from django.utils.text import slugify
from django.db import models
from django.conf import settings


class Status:
    OPEN = "OPEN"
    PROGRESS = "IN_PROGRESS"
    RESOLVED = "RESOLVED"


class Priority:

    LOW = "LOW"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"


class Issue(models.Model):

    STATUS_CHOICES = (
        (Status.OPEN, "Open"),
        (Status.PROGRESS, "In Progress"),
        (Status.RESOLVED, "Resolved"),
    )

    PRIORITY_CHOICES = (
        (Priority.LOW, "Low"),
        (Priority.MEDIUM, "Medium"),
        (Priority.HIGH, "High"),
    )

    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=120)
    description = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, default=Status.OPEN)
    priority = models.CharField(choices=PRIORITY_CHOICES, default=Priority.LOW)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="created_issues",
    )
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="assigned_issues",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("created_at",)

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def can_edit(self, user):
        return user.is_staff or self.created_by == user
    
    def can_delete(self,user):
        return self.created_by == user

    def can_change_status(self,user):
        return self.assigned_to == user
