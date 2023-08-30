from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

# Create your views here.
def product_create_view(request):
    context = {}
    form = ProductForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        # login required
        if request.user.is_authenticated:
            obj.user = request.user
            obj.save()
            return redirect('/products/create/')
        
        form.add_error(None, "You must be logged in to create products")

    context['form'] = form
    return render(request, 'products/create.html', context)

def product_list_view(request):
    # fetch all products from db
    object_list = Product.objects.all()

    return render(request, "products/list.html", {"object_list": object_list})

#views product using handle
def product_detail_view(request, handle=None):
    obj = get_object_or_404(Product, handle=handle)
    is_owner = False
    if request.user.is_authenticated:
        is_owner = obj.user = request.user     
    context = {"object": obj}
    if is_owner:       
        # owner can update product
        form = ProductForm(request.POST or None, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            # return redirect('/products/create/')
        context['form'] = form
    return render(request, 'products/detail.html', context)

