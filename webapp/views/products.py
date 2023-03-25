from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView, FormView
from webapp.models.products import Product
from webapp.forms import ProductForm


class ProductCreateView(LoginRequiredMixin, CreateView):
    template_name = 'product_add.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'product_update.html'
    form_class = ProductForm
    model = Product
    # success_message = "Продукт обновлен"
    # groups = ['admin', 'manager']
    # permission_required = "webapp.change_project"
    # permission_denied_message = "У вас не хватает прав доступа"

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'product_confirm_delete.html'
    model = Product
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class ProductDetailView(DetailView):
    template_name = 'product_detail.html'
    model = Product

