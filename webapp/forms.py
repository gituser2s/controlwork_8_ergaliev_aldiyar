from django import forms
from webapp.models.products import Product
from webapp.models.reviews import Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = {'title', 'category', 'description', 'image'}
        labels = {
            'title': 'Название',
            'category': 'Категория',
            'image': 'Картинка',
            'description': 'Описание',
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = {'text', 'score'}
        labels = {
            'text': 'Отзыв',
            'score': 'Оценка',
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='Найти')

