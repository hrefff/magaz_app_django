from django import forms
from warehouse.models import Income, Inventory, Sale

class AddIncomeForm(forms.ModelForm):
    class Meta():
        model = Income
        fields = ['income_order', 'item_id', 'quantity']
        labels = {
            'income_order': 'Заказ на приемку',
            'item_id': 'Товар',
            'quantity': 'Количество',
        }
        widgets = {
            'income_order': forms.TextInput(attrs={'class': 'form-control row'}),
            'item_id': forms.Select(attrs={'class': 'form-select row'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control row'}),
        }
    # item_id = forms.ModelChoiceField(queryset=Item.objects.get_queryset(), empty_label='-- Выберите товар --', to_field_name="item_name")


class AddSaleForm(forms.ModelForm):
    class Meta():
        model = Sale
        fields = ['sale_order', 'item_id', 'quantity']
        labels = {
            'sale_order': 'Заказ на отгрузку',
            'item_id': 'Товар',
            'quantity': 'Количество',
        }
        widgets = {
            'sale_order': forms.TextInput(attrs={'class': 'form-control row'}),
            'item_id': forms.Select(attrs={'class': 'form-select row'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control row'}),
        }
