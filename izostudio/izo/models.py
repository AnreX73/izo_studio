from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(unique=True, max_length=100, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорию услуг'
        verbose_name_plural = '1.Категории услуг'
        ordering = ['id']


class Post(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Объявление')
    content = RichTextField(blank=True, verbose_name='Текст объявления')
    is_published = models.BooleanField(default=False, verbose_name='Публикация')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление. Опубликовано может быть только одно !'
        verbose_name_plural = '6.Объявление'
        ordering = ['id']


class Nav(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='элемент навигации')
    slug = models.SlugField(unique=True, max_length=100, db_index=True, verbose_name='URL')
    image = models.ImageField(upload_to="images", blank=True, verbose_name='Изображение')
    annotations1 = models.TextField(blank=True, verbose_name='первое значение')
    annotations2 = models.TextField(blank=True, verbose_name='второе значение ')
    annotations3 = models.TextField(blank=True, verbose_name='третье  значение ')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_service', kwargs={'service_slug': self.slug})

    class Meta:
        verbose_name = 'элемент навигации'
        verbose_name_plural = '5.Элементы навигации'
        ordering = ['id']


class Contacts(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='заголовок')
    slug = models.SlugField(unique=True, max_length=100, db_index=True, verbose_name='URL')
    image = models.ImageField(upload_to="images", blank=True, verbose_name='Изображение')
    annotations1 = RichTextField(blank=True, verbose_name='информация')
    annotations2 = models.TextField(blank=True, verbose_name='ссылка,если есть')
    is_header_published = models.BooleanField(default=False, verbose_name='Публикация в шапке сайта')
    is_published = models.BooleanField(default=False, verbose_name='Публикация в контактах, карты-не отмечать!!!')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_service', kwargs={'service_slug': self.slug})

    class Meta:
        verbose_name = 'контакты '
        verbose_name_plural = '6.Контакты'
        ordering = ['id']


class Services(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    slug = models.SlugField(unique=True, max_length=100, db_index=True, verbose_name='URL')
    menu_image = models.ImageField(upload_to="images", verbose_name='Изображение в меню')
    page_image = models.ImageField(upload_to="images", verbose_name='Изображение на странице')
    annotation = models.TextField(blank=True, verbose_name='Рекламное описание ')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_service', kwargs={'service_slug': self.slug})

    class Meta:
        verbose_name = 'Фотоуслуги и сувениры'
        verbose_name_plural = '2.Фотоуслуги и сувениры'
        ordering = ['time_create', 'title']


class Prices(models.Model):
    service = models.ForeignKey(Services, on_delete=models.PROTECT, verbose_name='Услуга')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, max_length=100, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Цены')
    extraLink = models.CharField(blank=True, max_length=100, verbose_name='Ссылка на дополнительную информацию(если '
                                                                          'есть)')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Цены'
        verbose_name_plural = '3.Цены'
        ordering = ['id']


class Extra(models.Model):
    extraContent = models.ForeignKey(Prices, on_delete=models.PROTECT, verbose_name='Дополнительня информация о...')
    extra_image = models.ImageField(upload_to="images", blank=True, verbose_name='Изображение если есть')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, max_length=100, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Подробное описание')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_service', kwargs={'service_slug': self.slug})

    class Meta:
        verbose_name = 'Дополнительную информацию'
        verbose_name_plural = '4.Дополнительная информация'
        ordering = ['id']
