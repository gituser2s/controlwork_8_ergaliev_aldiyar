from django.urls import path
from webapp.views.base import IndexView
from webapp.views.products import ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView
from webapp.views.reviews import ReviewCreateView, ReviewUpdateView, ReviewDeleteView


urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("product/add/", ProductCreateView.as_view(), name="product_add"),
    path("product/<int:pk>", ProductDetailView.as_view(), name="product_detail"),
    path("product/<int:pk>/update", ProductUpdateView.as_view(), name="product_update"),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/confirm_delete/', ProductDeleteView.as_view(), name='product_confirm_delete'),
    path('product/<int:pk>/review', ReviewCreateView.as_view(), name="review_add"),
    path('review/<int:pk>/update', ReviewUpdateView.as_view(), name="review_update"),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name="review_delete"),
    path('review/<int:pk>/confirm_delete/', ReviewDeleteView.as_view(), name='review_confirm_delete'),
]

