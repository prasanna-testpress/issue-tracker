from django.urls import path
from .views import (
    AssignedIssueListView,
    CreatedIssueListView,
    CreateIssueView,
    DeleteIssueView,
    DetailedView,
    EditIssueView,
)

app_name = "issues"
urlpatterns = [
    path("", AssignedIssueListView.as_view(), name="mine"),
    path("created/", CreatedIssueListView.as_view(), name="created"),
    path("create/", CreateIssueView.as_view(), name="create"),
    path("<int:pk>/edit/", EditIssueView.as_view(), name="edit"),
    path("<int:pk>/delete/", DeleteIssueView.as_view(), name="delete"),
    path("<int:pk>/detail", DetailedView.as_view(), name="detail"),
]
