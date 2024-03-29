from django.contrib import admin
from .models import *

'''Модель карусель фото'''
admin.site.register(Carusel)

'''Модель контакт'''
admin.site.register(Contact)

'''Модель вопросы'''
admin.site.register(Question)

'''Модель о нас'''
admin.site.register(Onas)

'''Модель социальные сети'''
admin.site.register(Network)

'''Модель новости'''
admin.site.register(News)

'''Модель Title'''
admin.site.register(Setting)

'''Модель описание товара'''
admin.site.register(OpisanieProduct)

'''Модель товар'''
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'stock', 'available', 'hit_prodaj', 'hit_prodaj2', 'recomend', 'recomend2',
                    'new_tovar', 'new_tovar2', 'carusel_home_page', 'baher_glav1', 'carusel_home_page2', 'big_banner_glav_vnizy',
                    'big_recomend', 'big_new_tovar', 'specpredlojenie']
    list_filter = ['available']
    list_editable = [ 'stock', 'available']
    search_fields = ['name']

admin.site.register(Product, ProductAdmin)


class KategoryAdmin(admin.ModelAdmin):
    list_display = ['title_kategory', 'slug', 'id']
    prepopulated_fields = {'slug': ('title_kategory', )}

admin.site.register(Kategory, KategoryAdmin)