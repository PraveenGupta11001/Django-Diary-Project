# Create your views here.
# entries/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.views import View
from .models import Entry
from django.shortcuts import render
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class LockedView(LoginRequiredMixin):
    login_url = "admin:login"

class EntryListView(LockedView, ListView):
    model = Entry
    queryset = Entry.objects.all().order_by("-date_created")

class EntryDetailView(LockedView, DetailView):
    model = Entry
    template_name = "entries/entry_detail.html"

# class GetEntry(View):
#     queryset = Entry.objects.all()
#     def get(self, request, pk=None):
#         if pk :
#             entry = Entry.objects.get(pk=pk)
#             return render(request, "entries/entry_detail.html", {"entry" : entry})
#         else:
#             return render(request, "entries/entry_list.html", {"entry_list" : self.queryset})
        

#     def post(self, request):
#         pass

#     def put(self, request, pk):
#         pass

#     def delete(self, request, pk):
#         pass


# entries/views.py

class EntryCreateView(LockedView, SuccessMessageMixin, CreateView):
    model = Entry
    fields = ["title", "content"]
    success_url = reverse_lazy("entry-list")
    success_message = "Your new entry was created!"

class EntryUpdateView(LockedView, SuccessMessageMixin, UpdateView):
    model = Entry
    fields = ["title", "content"]
    success_message = "Your entry was updated!"

    def get_success_url(self):
        return reverse_lazy(
            "entry-detail",
            kwargs={"pk": self.object.id}
        )

class EntryDeleteView(LockedView, DeleteView):
    model = Entry
    success_url = reverse_lazy("entry-list")
    success_message = "Your entry was deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
    

    
    
# class EntryDetailOnlyView(View):

#     def get(self, request):
#         request.session["my_username"] = "Praween"
#         request.user
#         queryset = Entry.objects.all().order_by("-date_created")

#         return render(request, "my.html", {"qyerset" : queryset})


# def EntryDetail(request):

#     if request.POST:
#         pass
#     else:
#         request.session["my_username"] = "Praween"
#         request.user
#         queryset = Entry.objects.all().order_by("-date_created")

#         return render(request, "my.html", {"qyerset" : queryset})