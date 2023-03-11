from django import forms
from django.core.exceptions import ValidationError

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:

        model = Product
        fields = ('name', 'desc', 'img_link', 'category_name', 'price')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'desc': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'img_link': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'category_name': forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'price': forms.NumberInput(attrs={'class': 'form-control form-control-lg'})
        }
        labels = {
            'name': 'Наименование товара',
            'desc': 'Описание',
            'img_link': 'Ссылка на изображения',
            'category_name': 'Категория',
            'price': 'Цена',
        }

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['name'] == cleaned_data['desc']:
            raise ValidationError("Наименование и описание задачи не должны совпадать")
        if len(cleaned_data['name']) < 2 or len(cleaned_data['desc']) < 2:
            raise ValidationError("Длина поле должна быть больше двух символов")
        return cleaned_data


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False)
