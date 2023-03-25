from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView, View
from webapp.models.reviews import Review
from webapp.forms import ReviewForm


class ReviewCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.product_id = pk
            form.author = request.user
            form.save()
        return redirect('index')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class ReviewDetailView(DetailView):
    template_name = 'product_detail.html'
    model = Review


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'review_confirm_delete.html'
    model = Review
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'review_update.html'
    form_class = ReviewForm
    model = Review
    success_message = "Продукт обновлен"
    groups = ['admin', 'manager']
    permission_required = "webapp.change_project"
    permission_denied_message = "У вас не хватает прав доступа"

    def get_success_url(self):
        return reverse('index')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)
