from django.db import models
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.contrib.auth.models import User
import nepali_datetime


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 200, db_index = True) 
    slug = models.SlugField(max_length= 200, unique = True)
    image = models.ImageField(upload_to = 'category', blank = True, null= True)
    objects = models.Manager()
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name
    
    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.slug = slugify(self.name)
    #     super(Category, self).save(*args, **kwargs)
    
    # def get_absolute_url(self):
    #     return reverse("shop:product_list_by_category", args=[self.slug])

class SubCategory(models.Model):
    name = models.CharField(max_length = 200, db_index = True) 
    category = models.ForeignKey(Category, related_name='sub_category', on_delete=models.CASCADE)
    slug = models.SlugField(max_length= 200, unique = True)
    image = models.ImageField(upload_to = 'subcategory', blank = True, null= True)
    objects = models.Manager()
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategory'
        
    def __str__(self):
        return self.name
    
    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.slug = slugify(self.name)
    #     super(SubCategory, self).save(*args, **kwargs)

class News(models.Model):   
    title = models.CharField(max_length=300, db_index=True)
    slug = models.SlugField(max_length= 300, unique=True, null = True, blank = True)
    category = models.ForeignKey(Category, related_name= 'news', on_delete= models.CASCADE)
    image = models.ImageField(upload_to = 'News/%Y/%m/%d', blank = True)
    short_description = models.CharField(max_length=300, null = True, blank= True)
    description = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    added_by = models.ForeignKey(User, related_name = 'added_by_user', on_delete=models.CASCADE)
    status = models.CharField(max_length = 200, choices = (
        ('Hot', 'Hot'),
        ('Trending', 'Trending'),
        ('Latest', 'Latest'),
        ('Normal', 'Normal')
    ), default = 'Normal')
    sponsor = models.BooleanField(default=False)
    world_wide = models.BooleanField(default=False)
    total_visit = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    like = models.IntegerField(default=0)

   
    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)
        
    def __str__(self):
        return self.title

    def nepali_date(self):
        return nepali_datetime.date(2079,1,2).strftime('%K-%n-%D (%k %N %G)')
    
    # def save(self, *args, **kwargs):
    #     translator = Translator()
    #     translation = translator.translate(self.title)
    #     if not self.id:
    #         self.slug = slugify(translation)
    #     super(News, self).save(*args, **kwargs)
        
    # def get_absolute_url(self):
    #     return reverse("shop:productDetails", args=[self.slug, self.id])

class Advertisement(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='advertisement/', null = True, blank= True)
    description = RichTextUploadingField()

    
    def __str__(self):
        return self.name