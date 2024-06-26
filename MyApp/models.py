from unittest import result
from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File

# Create your models here.
class Faq(models.Model):
    Question = models.CharField(max_length=255)
    description=models.TextField(blank=True,null=True)
    date_added=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=("-date_added",)
    
    def __str__(self) -> str:
        return self.Question

class Testemonial(models.Model):
    tittle = models.CharField(max_length=255)
    description=models.TextField(blank=True,null=True)
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=("-date_added",)
    
    def __str__(self) -> str:
        return self.tittle


class Blog(models.Model):
    tittle= models.CharField(max_length=255)
    slug= models.SlugField()
    card_text=models.TextField(blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to='uploads/',blank=True,null=True)
    thumbnail=models.ImageField(upload_to='uploads/',blank=True,null=True)
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=("-date_added",)
    
    def __str__(self) -> str:
        return self.tittle
    
    def get_absolute_url(self):
        return f'/{self.slug}'
    
    def get_image(self):
        if self.image:
            return self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            return ''
            # if self.image:
            #     self.thumbnail=self.make_thumbnail(self.image)
            #     self.save()
            #     return  self.thumbnail.url

            # else:
            #     return ''

    def make_thumbnail(self,image,size=(300,200)):
        img=Image.open(image)
        img.convert("RGB")
        img.thumbnail(size)
        thumb_io=BytesIO()
        img.save(thumb_io,'JPEG',quality=85)
        thumbnail=File(thumb_io,name=image.name)
        return thumbnail


class Course(models.Model):  
    tittle= models.CharField(max_length=255)
    slug= models.SlugField()
    description=models.TextField(blank=True,null=True)
    price_per_month=models.IntegerField(null=True)
    classes_per_month=models.IntegerField(null=True)
    total_duration_in_minutes=models.IntegerField(null=True)
    durantion_in_months = models.CharField(max_length=255)
    learning_targets=models.TextField(blank=True,null=True)
    pre_requisites=models.TextField(blank=True,null=True)
    homework=models.TextField(blank=True,null=True)
    scheduling=models.TextField(blank=True,null=True)
    description_2=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to='uploads/',blank=True,null=True)
    thumbnail=models.ImageField(upload_to='uploads/',blank=True,null=True)
    date_added=models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering=("-date_added",)
    
    def __str__(self) -> str:
        return self.tittle
    
    def get_absolute_url(self):
        return f'/{self.slug}'
    
    def get_image(self):
        if self.image:
            return self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            return ''
            # if self.image:
            #     self.thumbnail=self.make_thumbnail(self.image)
            #     self.save()
            #     return  self.thumbnail.url

            # else:
            #     return ''

    def make_thumbnail(self,image,size=(300,200)):
        img=Image.open(image)
        img.convert("RGB")
        img.thumbnail(size)
        thumb_io=BytesIO()
        img.save(thumb_io,'JPEG',quality=85)
        thumbnail=File(thumb_io,name=image.name)
        return thumbnail
