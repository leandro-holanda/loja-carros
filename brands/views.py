from django.urls import reverse_lazy
from django.views import generic

from brands.forms import BrandForm
from brands.models import Brand


class BrandListView(generic.ListView):
    model = Brand
    context_object_name = 'brands'
    template_name = 'brands_list.html'
    paginate_by = 20


class BrandCreateView(generic.CreateView):
    model = Brand
    template_name = 'brands_create.html'
    form_class = BrandForm
    success_url = reverse_lazy('brand_list')


class BrandDetailView(generic.DetailView):
    model = Brand
    template_name = 'brands_detail.html'


class BrandUpdateView(generic.UpdateView):
    model = Brand
    template_name = 'brands_update.html'
    form_class = BrandForm
    success_url = reverse_lazy('brand_list')


class BrandDeleteView(generic.DeleteView):
    model = Brand
    template_name = 'brands_delete.html'
    form_class = BrandForm
    success_url = reverse_lazy('brand_list')
