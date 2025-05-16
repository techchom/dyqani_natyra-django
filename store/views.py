from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ReviewRating, ProductGallery
from category.models import Category



def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        
        

   



def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e


    # Get the reviews
    reviews = ReviewRating.objects.filter(product_id=single_product.id, status=True)

    # Get the product gallery
    product_gallery = ProductGallery.objects.filter(product_id=single_product.id)

    context = {
        'single_product': single_product,
       
        'reviews': reviews,
        'product_gallery': product_gallery,
    }
    return render(request, 'store/product_detail.html', context)


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        
            
    context = {
    }
    return render(request, 'store/store.html', context)

