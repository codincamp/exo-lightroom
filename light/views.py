from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.detail import SingleObjectMixin
from django.core.urlresolvers import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from .models import Light
from .forms import LightForm

from json_views.views import JSONListView, JSONFormView

class LightListView(ListView):
    model = Light

    def get_context_data(self, **kwargs):
        context = super(LightListView, self).get_context_data(**kwargs)

        lights = {}
        for light in self.get_queryset():
            lights[light] = LightForm(instance=light)

        context["object_list"] = lights

        #AJOUTE UN LIGHTFORM DANS LE CONTEXTE TEMPLATES
        context["lightform"] = LightForm()

        return context

class LightCreateView(CreateView):
    model = Light
    form_class = LightForm
    success_url = reverse_lazy('light-list')

class LightUpdateView(UpdateView):
    model = Light
    form_class = LightForm
    success_url = reverse_lazy('light-list')


class LightJSONListView(JSONListView):
    model = Light

    def get_context_data(self, **kwargs):
        context = super(LightJSONListView, self).get_context_data(**kwargs)
        lights = {}
        for light in self.get_queryset():
            lights[light.id] = LightForm(instance=light)

        context["lights"] = lights
        context["lightform"] = LightForm()

        return context

class LightJSONCreateView(JSONFormView):
    form_class = LightForm

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(LightJSONCreateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        light = form.save()
        return self.render_to_response(self.get_context_data(success=True, light=light))

class LightJSONUpdateView(JSONFormView):
    form_class = LightForm

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(LightJSONUpdateView, self).dispatch(request, *args, **kwargs)

    def get_form(self):
        return LightForm(self.request.POST, instance=self.light)

    def form_valid(self, form):
        light = form.save()
        return self.render_to_response(self.get_context_data(success=True,
                                       light=light,
                                       form=form))

    def post(self, request, *args, **kwargs):
         self.light = Light.objects.get(id=kwargs["pk"])
         return super(LightJSONUpdateView, self).post(request, *args, **kwargs)
