from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Onas, Product, Contact, Onas, News, Carusel, Kategory, Network, Setting
from .utils import get_constanta


# Страница дом
def home_page(request):
    home = Onas.objects.all()
    products = Product.objects.filter(available=True)
    kategory = Kategory.objects.all()
    news = News.objects.all()
    carusel = Carusel.objects.all()
    big_hit_prodaj = Product.objects.filter(big_hit_prodaj=True)
    hit_prodaj = Product.objects.filter(hit_prodaj=True)
    hit_prodaj2 = Product.objects.filter(hit_prodaj2=True)
    big_recomend = Product.objects.filter(big_recomend=True)
    recomend = Product.objects.filter(recomend=True)
    recomend2 = Product.objects.filter(recomend2=True)
    big_new_tovar = Product.objects.filter(big_new_tovar=True)
    new_tovar = Product.objects.filter(new_tovar=True)
    new_tovar2 = Product.objects.filter(new_tovar2=True)
    baher_glav1 = Product.objects.filter(baher_glav1=True)
    carusel_home_page = Product.objects.filter(carusel_home_page=True)
    carusel_home_page2 = Product.objects.filter(carusel_home_page2=True)
    big_banner_glav_vnizy = Product.objects.filter(big_banner_glav_vnizy=True)

    specpredlojenie = Product.objects.filter(specpredlojenie=True)
    samie_prodavaemie = Product.objects.filter(samie_prodavaemie=True)

    context = {
        'home': home,
        'products': products,
        'kategory': kategory,
        'news': news,
        'big_hit_prodaj': big_hit_prodaj,
        'hit_prodaj': hit_prodaj,
        'hit_prodaj2': hit_prodaj2,
        'big_recomend': big_recomend,
        'recomend': recomend,
        'recomend2': recomend2,
        'carusel': carusel,
        'baher_glav1': baher_glav1,
        'carusel_home_page': carusel_home_page,
        'carusel_home_page2': carusel_home_page2,
        'big_banner_glav_vnizy': big_banner_glav_vnizy,
        'big_new_tovar': big_new_tovar,
        'new_tovar': new_tovar,
        'new_tovar2': new_tovar2,
        'specpredlojenie': specpredlojenie,
        'samie_prodavaemie': samie_prodavaemie,
        **get_constanta(),
    }
    return render(request, 'polls/home_page.html', context)


# Новости
def news(request):
    products = Product.objects.filter(available=True)
    news = News.objects.all()

    paginator = Paginator(news, 3)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        'products': products,
        'news': queryset,
        **get_constanta(),
        }
    return render(request, 'polls/news.html', context)

#страница одной новости
def new_detail(request, id):
    new_detail = get_object_or_404(News, id=id)
    context = {
        'new_detail': new_detail,
        **get_constanta(),
        }
    return render(request, 'polls/new_detail.html',  context)

# О Нас 
def onas(request):
    onas = Onas.objects.all()
    context = {
        'onas': onas,
        **get_constanta(),
        }
    return render(request, 'polls/onas.html', context)

# Контакты
def contact(request):
    context = {
        **get_constanta(),
        }
    return render(request, 'polls/contact.html', context)


#страница товара
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    categories = Kategory.objects.filter(product=product)

    context = {
        'product': product,
        'categories': categories,
        **get_constanta(),
    }
    return render(request, 'polls/product_detail.html',  context)

#страница одной категории 
def kategory_detail(request, slug):
    kategory_detail = get_object_or_404(Kategory, slug=slug)
    products = kategory_detail.product.all()

    paginator = Paginator(products, 5)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
    'kategory_detail': kategory_detail,
    'products': queryset,
    **get_constanta(),
    }
    return render(request, 'polls/category_detail.html',  context)

#Поиск товара
def search_view(request):
    query = request.GET.get('q')  # Получаем запрос из параметра 'q' в GET-запросе
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        products = Product.objects.none()

    context = {
        **get_constanta(),
        'query': query,
        'products': products,
    }
    return render(request, 'polls/search_results.html', context)