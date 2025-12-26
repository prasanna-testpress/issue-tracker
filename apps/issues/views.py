from dataclasses import field
from .models import Issue
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView, DetailView, UpdateView,CreateView
from django.urls import reverse_lazy

class AssignedIssueListView(ListView,LoginRequiredMixin):

    model = Issue
    paginate_by = 10
    context_object_name='issues'
    extra_context={'title':'Assigned To me'}
    template_name='issues/issue_list.html'
    
    def get_queryset(self):
        return Issue.objects.filter(assigned_to=self.request.user)

class CreatedIssueListView(ListView,LoginRequiredMixin):

    model = Issue
    paginate_by = 10
    context_object_name='issues'
    template_name='issues/issue_list.html'
    extra_context={'title':'Created by me'}
    
    def get_queryset(self):
        return Issue.objects.filter(created_by=self.request.user)

class CreateIssueView(CreateView, LoginRequiredMixin):

    model = Issue
    success_url = reverse_lazy('issues:created')
    template_name= 'issues/issue_create.html'
    fields = ('title','description','priority','assigned_to')


    def form_valid(self,form):

        form.instance.created_by =  self.request.user        
        return super().form_valid(form)

    def get_queryset(self):
        return Issue.objects.filter(created_by=self.request.user)

class EditIssueView(UpdateView,LoginRequiredMixin):

    model = Issue
    success_url = reverse_lazy('issues:created')
    template_name= 'issues/issue_edit.html'
    fields = ('title','description','priority','assigned_to')
    
    def get_queryset(self):
        return Issue.objects.filter(created_by=self.request.user)

class DeleteIssueView(UpdateView,LoginRequiredMixin):

    model = Issue
    success_url = reverse_lazy('issues:created')
    template_name= 'issues/issue_confirm_delete.html'
    context_object_name='issue'

    def get_queryset(self):
        return Issue.objects.filter(created_by=self.request.user)

class DetailedView(DetailView, LoginRequiredMixin):
 
    model = Issue
    template_name= 'issues/issue_detail.html'
    context_object_name='issue'

