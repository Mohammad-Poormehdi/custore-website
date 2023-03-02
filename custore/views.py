from django.shortcuts import render
from django.db.models import Q
from custore.models import Product, Category, Size, Cart
# Create your views here.


def custore_home(request):
    products = Product.objects.all().order_by('-id')
    best_seller = Product.objects.all().order_by('-price')
    trends = Product.objects.all().order_by('quantity')
    context = {'products':products, 'best_seller':best_seller, 'trends':trends}
    return render(request, 'custore/home.html', context)

def shop(request):
    search = ''
    if request.GET.get('search-query'):
        search = request.GET.get('search-query')
    sizes = Size.objects.all()
    categorry_filter = Category.objects.filter(name__icontains=search)
    size_filter = Size.objects.filter(size__iexact=search)
    products = Product.objects.distinct().filter(Q(name__icontains = search)|
                                                 Q(category__in = categorry_filter)|
                                                 Q(size__in=size_filter))
    categorys = Category.objects.all()
    context = {'categorys':categorys, 'products':products, 'sizes':sizes}
    return render(request, 'custore/shop.html', context)

def cart(request):
    cart = Cart.objects.get(id=1)
    products = cart.product.all()
    context = {'products':products}
    return render(request, 'custore/cart.html', context)

def pages(request):
    return render(request, 'custore/pages.html')

def contact(request):
    return render(request, 'custore/contact.html')

def login_user(request):
    return render(request, 'custore/login.html')

def register_user(request):
    return render(request, 'custore/register.html')


