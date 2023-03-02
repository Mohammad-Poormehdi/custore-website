from django.contrib import admin
from custore.models import Product, Category, Size, Cart, Orders, Customer
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Size)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Orders)
