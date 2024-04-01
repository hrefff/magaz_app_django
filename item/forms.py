from django import forms
from item.models import Item

class AddItemForm(forms.ModelForm):
    class Meta():
        model = Item
        fields = ['item_name', 'description', 'groups']
        labels = {
            'item_name': 'Название',
            'description': 'Описание',
            'groups': 'Группы'
        }
        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'form-control row'}),
            'description': forms.TextInput(attrs={'class': 'form-control row'}),
            'groups': forms.CheckboxSelectMultiple()
        }

class EdirItemForm(forms.ModelForm):
    class Meta():
        model = Item
        fields = ['item_name', 'description', 'groups']
        labels = {
            'item_name': 'Название',
            'description': 'Описание',
            'groups': 'Группы'
        }
        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'form-control row'}),
            'description': forms.TextInput(attrs={'class': 'form-control row'}),
        }