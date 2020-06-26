from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from admin_manage.forms import Product
from .forms import OrderForm
from .forms import AddCart
from .models import Order_Item, Order

# Functions
def get_items_in_cart(request):
    products = []
    grand_total = 0
    index = 0
    quantity_total = 0
    mycart = []

    for item in request.session.get('cart'):
        product = Product.objects.get(pk=item['id'])

        quantity = int(item['stock'])
        total = quantity * (product.price / 100)
        grand_total += total

        quantity_total += quantity

        products.append({'id': product.id ,
            'name': product.name, 
            'price' : "{:12.2f}".format(product.price / 100), 
            'image': product.image, 
            'quantity': quantity, 
            'total': "{:12.2f}".format(total), 
            'index': index })
        index += 1

    grand_total_plus_shipping = grand_total 

    return (products, grand_total, quantity_total, grand_total_plus_shipping, )

# Create your views here.
def cart(request):
    
    (products, grand_total, quantity_total, grand_total_plus_shipping) = get_items_in_cart(request)

    context = {'products':products, 'grand_total_plus_shipping':"{:12.2f}".format(grand_total_plus_shipping), 
                    'quantity_total':quantity_total, 'grand_total':"{:12.2f}".format(grand_total)}

    return render(request, 'store/cart.html', context)

def checkout(request):
    (products, grand_total, quantity_total, grand_total_plus_shipping) = get_items_in_cart(request)
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        order = form.save(commit=False)

        order.status = 'PENDING STATUS'
        order.total = grand_total_plus_shipping

        order.save()

        for i in request.session.get('cart'):
            order_item = Order_Item(product_id=i['id'], quantity=i['stock'])
            order_item.save()
            order.order_list.add(order_item)
         
        del request.session['cart']
        request.session.modified = True

        return redirect('index')
    else:
        form = OrderForm()

    context = {'form':form, 'products':products,'grand_total_plus_shipping':"{:12.2f}".format(grand_total_plus_shipping), 
                    'quantity_total':quantity_total, 'grand_total':"{:12.2f}".format(grand_total)}
    
    return render(request, 'store/checkout.html', context)

def index(request):
    products = Product.objects.all()

    product_list = Paginator(products, 4)

    grouped_products = []
    for p in product_list.page_range:
        product_objects = product_list.page(p).object_list
        grouped_products.append(product_objects)

    context = {'products':products, 'grouped_products': grouped_products }

    print(grouped_products)

    return render(request, 'store/index.html', context)

def view_product(request, product_id):
    product  = Product.objects.get(pk=product_id)

    if request.method == 'POST':
        form = AddCart(request.POST, max_count=product.stock)

        if form.is_valid():
            if not 'cart' in request.session or not request.session['cart']:
                request.session['cart'] = [{ 'id': product.id, 'stock': form.cleaned_data['num_of_items']}]
                request.session.modified = True
            else:
                saved_list = request.session['cart']
                saved_list.append({ 'id': product.id, 'stock': form.cleaned_data['num_of_items']})
                request.session['cart'] = saved_list
                request.session.modified = True

            return redirect('index')
    else:
        form = AddCart(max_count=product.stock)

    product.price = "{:12.2f}".format(product.price / 100)

    context = {'product':product, 'form':form }

    return render(request, 'store/view-product.html', context)

def remove_from_cart(request, product_index):
     del request.session['cart'][int(product_index)]
     request.session.modified = True
     return redirect('cart')

def add_to_cart(request, item_id):
    product = Product.objects.get(pk=item_id)

    if not 'cart' in request.session or not request.session['cart']:
            request.session['cart'] = [{ 'id': product.id, 'stock': 1 }]
            request.session.modified = True
    else:
        saved_list = request.session['cart']
        saved_list.append({ 'id': product.id, 'stock': 1 })
        request.session['cart'] = saved_list
        request.session.modified = True

    return redirect('index')