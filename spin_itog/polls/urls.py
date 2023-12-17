from django.urls import path
from polls import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('news/', views.news, name='news'),
    path('news/<int:id>/', views.new_detail, name='new_detail'),
    path('onas/', views.onas, name='onas'),
    path('contact/', views.contact, name='contact'),

    path('category/<slug:slug>/', views.kategory_detail, name='category_detail'),

    path('product/<int:id>/', views.product_detail, name='product_detail'),

    path('search/', views.search_view, name='search'),

]