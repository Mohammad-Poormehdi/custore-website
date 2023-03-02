from django.shortcuts import render
from custore.models import Product, Orders, Customer
# Create your views here.

def inventory(request):
    search = ''
    if request.GET.get('search-query'):
        search = request.GET.get('search-query')
    products = Product.objects.filter(name__icontains=search).order_by('-id')
    print(products)
    context = {'products':products}
    return render(request, 'cms/cms_inventory.html', context)

def customers(request):
    search = ''
    if request.GET.get('search-query'):
        search = request.GET.get('search-query')
    customers = Customer.objects.filter(name__icontains=search)
    context = {'customers':customers}
    return render(request, 'cms/customers.html', context)

def orders(request):
    search = ''
    if request.GET.get('search-query'):
        search = request.GET.get('search-query')
    customer = Customer.objects.filter(name__icontains=search)
    orders = Orders.objects.filter(customer__in=customer)
    context = {'orders':orders}
    return render(request, 'cms/orders.html', context)