from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

#модель карусели на главной странице
class Carusel(models.Model):
    title_carusel = models.CharField(max_length=500, verbose_name='название карусели')
    carusel_image = models.ImageField(upload_to='network_image', blank=True, verbose_name='картинка карусель')
    carusel_text = models.TextField(blank=True, verbose_name='текст для карусели')

    class Meta:
        verbose_name = 'фото карусель'
        verbose_name_plural = 'фото карусель'

    def __str__(self):
        return self.title_carusel 

# Модель социальные иконки
class Network(models.Model):
    title_ikons = models.CharField(max_length=500, verbose_name='иконка соцсети')
    network_image = models.ImageField(upload_to='network_image', blank=True, verbose_name='картинка соцсети')
    url_network = models.TextField(blank=True, verbose_name='ссылка')

    class Meta:
        verbose_name = 'социальные сети'
        verbose_name_plural = 'социальные сети'

    def __str__(self):
        return self.title_ikons
    
 # Модель контактов   
class Contact(models.Model):
    title_contact = models.CharField(max_length=200, verbose_name='контакт')
    body_contact = RichTextUploadingField(blank=True, default='', verbose_name='текст контакта')
    adress_one_contact = models.TextField(blank=True, default='', verbose_name='адрес')
    tel = models.CharField(max_length=200, verbose_name='телефон')
    web = models.TextField(blank=True, default='', verbose_name='email')
    network_ikons = models.ManyToManyField(Network, blank=True, default='', verbose_name='иконки соцсетей')

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакт'

    def __str__(self):
        return self.title_contact
    
# Модель Новости    
class News(models.Model):
    title_new = models.CharField(max_length=200, verbose_name='заголовок новости')
    body_new = RichTextUploadingField(blank=True, default='', verbose_name='текст неовости')
    image_new = models.ImageField(upload_to='image_new', blank=True, verbose_name='картинка новости')

    class Meta:
        verbose_name = 'новости'
        verbose_name_plural = 'новости'

    def __str__(self):
        return self.title_new
    
# Модель часто задаваемых воросов
class Question(models.Model):
    title_question = models.CharField(max_length=500, verbose_name='вопрос')
    body_question = models.TextField(blank=True, default='', verbose_name='ответ')

    class Meta:
        verbose_name = 'вопросы'
        verbose_name_plural = 'вопросы'

    def __str__(self):
        return self.title_question

# Модель сертификатов 
class Sertificat(models.Model):
    title_sertificat = models.CharField(max_length=500, verbose_name="заголовок сертификата")
    image_sertificat = models.ImageField(upload_to='sertifacats', blank=True, verbose_name='фото сертификата')

    class Meta:
        verbose_name = 'сертификат'
        verbose_name_plural = 'сертификаты'

    def __str__(self):
        return self.title_sertificat
    
# Модель О Нас
class Onas(models.Model):
    title_onas1 = models.CharField(max_length=500, verbose_name='заголовок')
    title_onas2 = models.CharField(blank=True, max_length=500, verbose_name='второй заголовок')
    body_onas = RichTextUploadingField(blank=True, default='', verbose_name='текст')
    image_uslugi = models.ImageField(upload_to='home', blank=True, verbose_name='главное фото')
    image_sertifacat = models.ManyToManyField(Sertificat, blank=True, verbose_name='сертификаты')
    question = models.ManyToManyField(Question, verbose_name='вопрос')


    class Meta:
        verbose_name = 'онас'
        verbose_name_plural = 'онас'

    def __str__(self):
        return self.title_onas1
    

'''Модель продукта'''
class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение товара")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="На складе")
    reklam_title = models.TextField(blank=True, verbose_name="Рекламный заголовок")
    reklam_text = models.TextField(blank=True, verbose_name="Рекламный текст")
    skidka = models.TextField(blank=True, verbose_name="размер скидки")
    image_for_banner = models.ImageField(upload_to='banner/', blank=True, verbose_name="фото для баннера")

    available = models.BooleanField(default=True, verbose_name="Доступен")
    hit_prodaj = models.BooleanField(default=False, verbose_name="Хит продаж")
    hit_prodaj2 = models.BooleanField(default=False, verbose_name="Хит продаж2")
    big_hit_prodaj = models.BooleanField(default=False, verbose_name="Большая фото Хит продаж")
    recomend = models.BooleanField(default=False, verbose_name="Рекомендуемые")
    recomend2 = models.BooleanField(default=False, verbose_name="Рекомендуемые2")
    big_recomend = models.BooleanField(default=False, verbose_name="Большая фото Рекомендуемого товара")
    new_tovar = models.BooleanField(default=False, verbose_name="Новый товар")
    new_tovar2 = models.BooleanField(default=False, verbose_name="Новый товар2")
    big_new_tovar = models.BooleanField(default=False, verbose_name="Большая фото новый товар")
    carusel_home_page = models.BooleanField(default=False, verbose_name="баннер главная страница слева")
    carusel_home_page2 = models.BooleanField(default=False, verbose_name="баннер главная страница справа")
    baher_glav1 = models.BooleanField(default=False, verbose_name="баннер справа от карусели")
    big_banner_glav_vnizy = models.BooleanField(default=False, verbose_name="большой баннер на главной странице внизу")
    specpredlojenie = models.BooleanField(default=False, verbose_name="спецпредложение главная стр")
    samie_prodavaemie = models.BooleanField(default=False, verbose_name="самые продаваемые на главной странице")

    class Meta:
        ordering = ['name']
        index_together = ['id']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    @property
    def ct_models(self):
        return self._meta.model_name
    
# Модель Категории
class Kategory(models.Model):
    title_kategory = models.CharField(max_length=200, verbose_name='категория')
    slug = models.SlugField('slug')
    image_katalog = models.ImageField(upload_to='kategory/', verbose_name='фото категории', blank=True)
    product = models.ManyToManyField(Product, verbose_name='товар')

    class Meta:
        ordering = ['title_kategory']         
        index_together = [          
            ['id', 'slug']          
        ] 
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.title_kategory
    
#Модель title
class Setting(models.Model):
    objects = None
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayir')
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title



