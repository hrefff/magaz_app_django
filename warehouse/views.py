from unittest import result
from django.shortcuts import render
from warehouse.models import Income, Sale, Inventory, Report
from warehouse.forms import AddIncomeForm, AddSaleForm
from django.contrib.auth.decorators import user_passes_test
from django.db import connection

@user_passes_test(lambda u: u.is_superuser) # проверка на суперюзера
def income(request):
    incomes = Income.objects.all().order_by('-created')
    context = {'incomes': incomes}
    return render(request, "income.html", context)

@user_passes_test(lambda u: u.is_superuser)
def income_details(request, income_id):
    income = Income.objects.get(pk=income_id)
    context = {'income': income}
    return render(request, "income_details.html", context)

@user_passes_test(lambda u: u.is_superuser)
def add_income(request):
    if request.method == 'POST':
        form = AddIncomeForm(request.POST)
        if form.is_valid():
            # проверяем, есть ли принимаемый товар в складских запасах (Inventory)
            inv_item, created = Inventory.objects.get_or_create(item_id=form.cleaned_data['item_id'])
            if(created):
                # нет в запасах: тогда добавляем новую строку в Inventory
                inv_item.quantity = form.cleaned_data['quantity']
                # inv_item.save()
            else:
                # есть в запасах: увеличиваем его кол-во на form.quantity
                inv_item.quantity += form.cleaned_data['quantity']
            # сохраняем товар в складских запасах
            inv_item.save()
            # сохраняем заказ на приемку
            form.save()
            # формируем контекст
            context = {'result': 'Приемка успешно выполнена!'}
        else:
            context = {'form': form}
    else:
        context = {'form': AddIncomeForm}
    return render(request, "add_income.html", {'context': context})

@user_passes_test(lambda u: u.is_superuser)
def sale(request):
    sales = Sale.objects.all().order_by('-created')
    context = {'sales': sales}
    return render(request, "sale.html", context)

@user_passes_test(lambda u: u.is_superuser)
def sale_details(request, sale_id):
    sale = Sale.objects.get(pk=sale_id)
    context = {'sale': sale}
    return render(request, "sale_details.html", context)

@user_passes_test(lambda u: u.is_superuser)
def add_sale(request):
    if request.method == 'POST':
        form = AddSaleForm(request.POST)
        if form.is_valid():
            # проверяем, есть ли отгружаемый товар в складских запасах (Inventory)
            try:
                inv_item = Inventory.objects.get(item_id=form.cleaned_data['item_id'])
                if(inv_item):
                    # требуемое кол-во в заказе меньше или равно кол-ву в складских запасах
                    if(form.cleaned_data['quantity'] <= inv_item.quantity):
                        # уменьшаем кол-во в складских запасах на требуемое в заказе
                        inv_item.quantity -= form.cleaned_data['quantity']
                        # сохраняем изменения в складских запасах
                        inv_item.save()
                        # если кол-во в складских запасах стало равно 0, то удалить запись из складских запасов
                        if(inv_item.quantity == 0):
                            inv_item.delete()
                        # сохраняем заказ на отгрузкуч>
                        form.save()
                        context = {'result': 'Отгрузка успешно выполнена!'}
                    else:
                        # требуемое кол-во больше чем доступное в складских запасах
                        context = {'error': 'Запрошенное кол-во отсутствует на складе!', 'form': form}
            except:
                context = {'error': 'Запрошенный товар отсутствует на складе!','form': form}
        else:
            context = {'form': form}
    else:
        context = {'form': AddSaleForm}
    return render(request, "add_sale.html", {'context': context})

@user_passes_test(lambda u: u.is_superuser)
def inventory(request):
    inventories = Inventory.objects.all().order_by('item_id')
    context = {'inventories': inventories}
    return render(request, "inventory.html", context)

@user_passes_test(lambda u: u.is_superuser)
def report(request):
    reports = Report.objects.all().order_by('id')
    context = {'reports': reports}
    return render(request, "report.html", context)

@user_passes_test(lambda u: u.is_superuser)
def report_result(request, report_id):
    report = Report.objects.get(pk=report_id)
    print(report.code)
    result = run_custom_sql_fetchone(report.code)
    print(result)
    context = {'result': result[0], 'report': report}
    return render(request, "report-result.html", context)

def run_custom_sql_fetchone(sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        row = cursor.fetchone()
    return row
