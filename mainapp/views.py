from django.shortcuts import HttpResponse, render
from store.models import Product, Rating
from kart.settings import COMPANY, COMPANY_LOGO, COMPANY_BANN1, COMPANY_BANN2, COMPANY_BANN3, COMPANY_BANN4, COMPANY_BANN5, COMPANY_SLOGAN, COMPANY_SLOG_SUB1, COMPANY_SLOG_SUB2

# Create your views here.

def home(request):
    products = None
    ratings = None
    try:
        products = Product.objects.all().filter(is_available=True).order_by( '-created_at', '-has_discount')
        for product in products:
            ratings = Rating.objects.filter(product_id=product.id, status=True)
    except:
        None
    context = {
        'title': "Listado productos",
        'products': products,
        'ratings': ratings,
        'COMPANY': COMPANY,
        'COMPANY_LOGO' : COMPANY_LOGO,
        'COMPANY_BANN1': COMPANY_BANN1,
        'COMPANY_BANN2': COMPANY_BANN2,
        'COMPANY_BANN3': COMPANY_BANN3,
        'COMPANY_BANN4': COMPANY_BANN4,
        'COMPANY_BANN5': COMPANY_BANN5,
        'COMPANY_SLOGAN': COMPANY_SLOGAN,
        'COMPANY_SLOG_SUB1': COMPANY_SLOG_SUB1,
        'COMPANY_SLOG_SUB2': COMPANY_SLOG_SUB2,
    }
    return render(request, 'mainapp/home.html', context) # 'mainapp' subdirectorio en 'templates'