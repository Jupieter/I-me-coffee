from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
import datetime
from raw_material.models import ProductAcquisition
from .models import CoffeeMake, CoffeeOrder
from .forms import CoffeeMakerForm, CoffeeOrderForm


def coffee_home(request):
    return render(request, 'shop/coffee_home.html', {})

def coffee_make(request):
    wares1 = ProductAcquisition.objects.filter(store_status=3)
    stock_min = 40
    wares=[]
    dt= datetime.datetime.now().date()
    for ind, ware in enumerate(wares1):
        if ware.ware_type.ware_type.ware_types == 'Kávé':
            wares.append(ware)
    return render(request, 'shop/coffee_make.html', {'wares':wares,'dt':dt, 'stock_min':stock_min})


def coffee_make_form(request, pkey):
    ware = get_object_or_404(ProductAcquisition, pk=pkey)
    dose_weight = ware.ware_type.ware_type.ware_wght
    stock_min = 40
    alrt ='';    cm = None
    if  ware.stock < stock_min:
        alrt = "Nagyon kevés a kibontott anyag készlet. Kérem ellenőrizze!"
    dt= datetime.datetime.now()  
    if request.method == "POST":
        form = CoffeeMakerForm(request.POST)
        if form.is_valid():
            cm = form.cleaned_data
            dtd = cm['c_make_date'];  dtt = cm['c_make_time']
            dt_h = dtt.hour;  dt_m = dtt.minute
            dt_change = datetime.timedelta(hours=dt_h, minutes=dt_m)
            dtf = dtd + dt_change
            dt=[dtd, dtt, dtf]
            coffe_new = CoffeeMake(
                c_make_ware = ware,
                c_make_dose = cm['c_make_dose'],
                c_make_user = request.user,
                c_make_date = dtf,
                c_reg_time = timezone.now(),
                )
            coffe_new.save()
            wght = ware.stock
            ware.stock = wght - dose_weight * cm['c_make_dose']
            ware.save()
            
            # field_names = [f.name for f in CoffeeMake._meta.get_fields()]

            return redirect('shop:coffee_home')
            '''return render(request, 'shop/coffee_make_form.html', 
            {'form': form, 'ware':ware,'dt':dt, 'alrt':alrt,
             'stock_min':stock_min,'dt':dt, 'cm':cm, 
             'field_names':field_names, 'coffe_new':coffe_new })
        else:
            cm = form.cleaned_data
            return render(request, 'shop/coffee_make_form.html', 
            {'form': form, 'ware':ware,'dt':dt, 'alrt':alrt, 
            'stock_min':stock_min, 'dt':dt,'cm':cm, 'coffe_new':coffe_new})'''
    else:
        form = CoffeeMakerForm()
        form.fields['c_make_date'].initial = dt
    return render(request, 'shop/coffee_make_form.html', 
    {'form': form, 'ware':ware,'dt':dt, 'alrt':alrt, 'stock_min':stock_min})


def coffee_order(request):
    dt= datetime.datetime.now()
    dt_start = dt
    dt_end = dt + datetime.timedelta(days=1)
    coffees1 = CoffeeMake.objects.filter(c_make_date__range =(dt_start, dt_end))
    coffees = coffees1.order_by('id')
    adat = []
    for coffee in coffees:
        adat.append(coffee.id)
    coffees = coffees.order_by('c_make_date')
    ordered = CoffeeOrder.objects.filter(coffee_selected__in = adat)

    return render(request, 'shop/coffee_order.html', 
        {'coffees':coffees,'dt':dt, 'dt_end':dt_end, 'adat':adat, 'ordered':ordered})

def coffee_order_remove(request, pk):
    coffee1 = get_object_or_404(CoffeeOrder, pk=pk)
    coffee1.delete()
    return redirect('shop:coffee_order')

def coffee_order_form(request, pkey):
    proba = ''
    coffee_1 = get_object_or_404(CoffeeMake, pk=pkey)
    wares = ProductAcquisition.objects.filter(store_status=3)
    dose = coffee_1.c_make_dose
    sugar = []; milk = []; flavour = []; adat = []
    for ware in wares:
        if ware.ware_type.ware_type.ware_types == 'Cukor':
            dt1 = ware.id
            dt2 = ware
            dt = (dt1,dt2)
            sugar.append(dt)
        elif ware.ware_type.ware_type.ware_types == 'Tej': 
            dt1 = ware.id
            dt2 = ware
            dt = (dt1,dt2)
            milk.append(dt)
        elif ware.ware_type.ware_type.ware_types == 'Ízesítő': 
            dt1 = ware.id
            dt2 = ware
            dt = (dt1,dt2)
            flavour.append(dt)

    if request.method == "POST":
        form = CoffeeOrderForm(request.POST)
        if form.is_valid():
            coffee2 = form.save(commit=False)
            coffee2.coffee_selected = coffee_1
            coffee2.coffe_user = request.user
            coffee2.coffee_reg = timezone.now() 
            sugar_s = ProductAcquisition.objects.filter(pk=coffee2.sugar_choice.pk)
            milk_s = ProductAcquisition.objects.filter(pk=coffee2.milk_choice.pk)
            falvour_s = ProductAcquisition.objects.filter(pk=coffee2.flavour_choice.pk)
            proba = ' üres '
            # coffee2.save()
            coffee_1.c_make_dose = dose-coffee2.coffee_dose
            # coffee_1.save()
            # return redirect('shop:coffee_order')
            return  render(request, 'shop/c_order_form_copy.html',
                {'form': form, 'wares':wares, 'dose':dose, 'coffee_1':coffee_1, 'coffee2':coffee2,
                'sugas_s':sugar_s, 'milk_s':milk_s, 'falvour_s':falvour_s, 'proba':proba})
        else:
            coffee2 = form.save(commit=False)
            coffee2.coffee_selected = coffee_1
            coffee2.coffe_user = request.user
            coffee2.coffee_reg = timezone.now() 
            coffee_1.c_make_dose = dose-coffee2.coffee_dose
            sugar_s = ' az'
            milk_s = ' amaz '
            falvour_s = "else"
            proba = ProductAcquisition.objects.filter(pk=coffee2.milk_choice.pk)
            # coffee2.save()
            # coffee_1.save()
            # return redirect('shop:coffee_order')
            return  render(request, 'shop/c_order_form_copy.html',
                {'form': form, 'wares':wares, 'dose':dose, 'coffee_1':coffee_1, 'coffee2':coffee2,
                'sugas_s':sugar_s, 'milk_s':milk_s, 'falvour_s':falvour_s, 'proba':proba})

    else:
        form = CoffeeOrderForm()
        form.fields['sugar_choice'].choices  = sugar
        form.fields['sugar_choice'].initial  = [1]
        form.fields['milk_choice'].choices  = milk
        form.fields['milk_choice'].initial  = [1]
        form.fields['flavour_choice'].choices  = flavour
        form.fields['flavour_choice'].initial  = [1]
        form.fields['coffee_dose'].widget.attrs['max'] = dose
        proba = ProductAcquisition.objects.filter(pk=28)
        
    return render(request, 'shop/c_order_form.html',
        {'form': form, 'wares':wares, 'dose':dose, 'coffee_1':coffee_1,
        'sugar':sugar , 'milk':milk, 'falvour':flavour, 'proba':proba})