from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
from store.models import Order_Item, Order

# Create your views here.
def add_product(request):
    if request.method =='POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.price = form.cleaned_data['price'] * 100
            product.save()

            return redirect('admin_index')
    else:
        form = ProductForm()

    context = {'form':form}

    return render(request, 'admin_manage/add-product.html', context)

def index(request):
    products = Product.objects.all()
    orders = Order.objects.all()

    total_products = 0
    products_out_of_stock = 0
    products_in_stock = 0

    for p in products:
        p.price = "{:12.2f}".format(p.price / 100) # Displays price with 2 decimal places
        if p.stock > 0:
            products_in_stock = products_in_stock + 1
            total_products = total_products + p.stock
        elif p.stock < 1:
            products_out_of_stock = products_out_of_stock + 1

    context = {'products':products, 'products_in_stock': products_in_stock, 'total_products':total_products,
                    'orders':orders}
    return render(request, 'admin_manage/index.html', context)

def view_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    order_list = order.order_list.all()

    display_orders = []
    item_total = 0
    total = 0

    for o_list in order_list:
        user_product = Product.objects.get(pk=o_list.product_id)
        user_quantity = o_list.quantity
        item_total = user_product.price * user_quantity
        display_orders.append({'user_product': user_product, 'user_quantity':user_quantity, 'item_total':item_total })
        total = total + item_total


    context = {'order':order, 'display_orders':display_orders, 'total':total }

    return render(request, 'admin_manage/view-order.html', context)