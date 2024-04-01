from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from item.models import Item
from item.forms import AddItemForm

@user_passes_test(lambda u: u.is_authenticated)
def item(request):
    items = Item.objects.all().order_by('item_name')
    groups = request.GET.getlist('group')
    if(groups):
        print(groups)
        items = items.filter(groups__in=groups).distinct().order_by('item_name')
    context = {'items': items, 'groups': groups }
    return render(request, "item.html", context)

def item_details(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {'item': item}
    return render(request, "item_details.html", context)

@user_passes_test(lambda u: u.is_superuser)
def add_item(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'result': 'Товар успешно добавлен!'}
    else:
        context = {'form': AddItemForm}
    return render(request, "add_item.html", {'context': context})

@user_passes_test(lambda u: u.is_superuser)
def change_item(request, item_id):
    pass

@user_passes_test(lambda u: u.is_superuser)
def delete_item(request, item_id):

    try:
        item = Item.objects.get(pk=item_id)
        i = item.item_name
        print(item.item_name)
        print(i)
        item.delete()
        context = {'result': 'Товар "" удален!'}
    except:
        context = {'result': 'Ошибка удаления товара ""!'}
    return render(request, "item.html", context)