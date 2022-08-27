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
    cover = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='تصویر')

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'
        ordering = ['-created_date']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='پست')
    name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='نویسنده')
    body = models.TextField(verbose_name='متن')    
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'
        ordering = ['-created_date']

    def __str__(self):
        return f'{self.name}: {self.body}'
        