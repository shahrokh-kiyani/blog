from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from taggit.managers import TaggableManager

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام دسته بندی')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='آدرس دسته بندی')
    description = models.TextField(null=True, blank=True, verbose_name='توضیحات دسته بندی')


    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name





class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, verbose_name='سازنده')
    body = models.TextField(verbose_name='متن')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    modified_date = models.DateTimeField(auto_now=True, verbose_name='تاریخ تغییر')
    slug = models.SlugField(max_length=200, unique=True, null=True, verbose_name='آدرس')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name='دسته بندی')
    tags = TaggableManager(verbose_name='برچسب ها')

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})
