from django.urls import reverse_lazy
from django.views import generic

from models_car.forms import ModelCarForm
from models_car.models import ModelCar


class ModelCarListView(generic.ListView):
    model = ModelCar
    context_object_name = 'modelcars'
    template_name = 'modelcar_list.html'
    paginate_by = 20


class ModelCarCreateView(generic.CreateView):
    model = ModelCar
    template_name = 'modelcar_create.html'
    form_class = ModelCarForm
    success_url = reverse_lazy('modelcar_list')


class ModelCarDetailView(generic.DetailView):
    model = ModelCar
    template_name = 'modelcar_detail.html'


class ModelCarUpdateView(generic.UpdateView):
    model = ModelCar
    template_name = 'modelcar_update.html'
    form_class = ModelCarForm
    success_url = reverse_lazy('modelcar_list')


class ModelCarDeleteView(generic.DeleteView):
    model = ModelCar
    template_name = 'modelcar_delete.html'
    form_class = ModelCarForm
    success_url = reverse_lazy('modelcar_list')
