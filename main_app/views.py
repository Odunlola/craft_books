from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.views.generic.base import TemplateView
from .models import Craft
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

class Home(TemplateView):
    template_name = "home.html"
    
class About(TemplateView):
 template_name = "about.html"


class CraftList(TemplateView):
    template_name = "craft_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        type = self.request.GET.get("type")
        if type!= None:
            context["cratfs"] = Craft.objects.filter(type__icontains=type)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {type}"
        else:
           context["crafts"] = Craft.objects.all()
           context["header"] = "My Favorite Craftsy-Arts"
        return context
    
class CraftCreate(CreateView):
    model = Craft
    fields = ['type', 'img', 'about', 'verified_craft']
    template_name = "craft_create.html"
    # success_url = "/crafts/"
    def get_success_url(self):
        return reverse('craft_detail', kwargs={'pk': self.object.pk})

class CraftDetail(DetailView):
    model = Craft
    template_name = "craft_detail.html"

class CraftUpdate(UpdateView):
    model = Craft
    fields = ['type', 'img', 'bio', 'verified_artist']
    template_name = "craft_update.html"
    success_url = "/crafts/"

class CraftDelete(DeleteView):
    model = Craft
    template_name = "craft_delete_confirmation.html"
    success_url = "/crafts/"