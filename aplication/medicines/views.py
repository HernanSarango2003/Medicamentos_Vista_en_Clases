from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Medicamento
from .forms import MedicamentoForm
from django.contrib.auth.mixins import LoginRequiredMixin  # Importa el mixin para requerir autenticación


class MedicamentoListView(ListView):
    template_name = "medicamento/list.html"
    model = Medicamento
    context_object_name = "medicamentos"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Medicamentos"
        context['title1'] = "Listado de Medicamentos"
        return context

class MedicamentoCreateView(LoginRequiredMixin, CreateView):  # Agrega LoginRequiredMixin
    model = Medicamento
    form_class = MedicamentoForm
    template_name = "medicamento/form.html"
    success_url = reverse_lazy("medicines:medicamento_list")

    def form_valid(self, form):
        form.instance.registered_by = self.request.user  # Asigna el usuario actual al campo registered_by
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Medicamentos"
        context['title1'] = "Añadir Medicamento"
        return context

class MedicamentoUpdateView(UpdateView):
    model = Medicamento
    form_class = MedicamentoForm
    template_name = "medicamento/form.html"
    success_url = reverse_lazy("medicines:medicamento_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Medicamentos"
        context['title1'] = "Editar Medicamento"
        return context

class MedicamentoDeleteView(DeleteView):
    model = Medicamento
    template_name = "medicamento/delete.html"
    success_url = reverse_lazy("medicines:medicamento_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminar"
        context['title1'] = "Eliminar Medicamento"
        return context
