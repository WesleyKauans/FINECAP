from django.shortcuts import render
from .models import Reserva
from .form import ReservaForm
from django.views.generic import ListView,CreateView,DeleteView,DetailView, UpdateView,TemplateView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.messages import views


class Index(generic.TemplateView):
    template_name = "reserva/index.html"
    
    
class Detalhar(DetailView):
    model = Reserva
    template_name = "reserva/detalhar.html"  
    context_object_name = 'reserva'

class Listar(ListView):
    template_name = "reserva/reservas.html"
    model = Reserva
    context_object_name = 'reserva'
    paginate_by = 3


class Cadastrar(views.SuccessMessageMixin, generic.CreateView):
  model = Reserva
  form_class = ReservaForm
  template_name = "reserva/forms.html"
  success_url = reverse_lazy("listar")
  success_message = "Reserva cadastrada com sucesso!"
  
class Deletar(views.SuccessMessageMixin, generic.DeleteView):
  model = Reserva
  template_name = "reserva/deletar.html"
  success_url = reverse_lazy("listar")
  success_message = "Reserva removida com sucesso!"
  
class Editar(views.SuccessMessageMixin, generic.UpdateView):
  model = Reserva
  form_class = ReservaForm
  template_name = "reserva/forms.html"
  success_url = reverse_lazy("listar")
  success_message = "Reserva atualizada com sucesso! " 