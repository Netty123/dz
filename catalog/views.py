from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Phone

def catalog(request):
    sort_param = request.GET.get('sort', '')
    
    if sort_param == 'name':
        phones = Phone.objects.all().order_by('name')
    elif sort_param == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif sort_param == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    else:
        phones = Phone.objects.all()
    
    context = {
        'phones': phones,
        'current_sort': sort_param,
    }
    return render(request, 'catalog.html', context)

def phone_detail(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    context = {'phone': phone}
    return render(request, 'phone_detail.html', context)
