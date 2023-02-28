from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.urls import reverse
from uuid import uuid4
from django_resized import ResizedImageField
from django.utils.translation import gettext as _
import os 


# Create your models here.
class Profile(models.Model):
        SUBSCRIPTION_OPTIONS = [
        ('free', 'free'),
        ('starter', 'starter'), 
        ('advanced', 'advanced'), 
        ]
        user = models.OneToOneField(User,on_delete=models.CASCADE)
        first_name = models.CharField(null=True, blank=True, max_length=100)
        last_name = models.CharField(null=True, blank=True, max_length=100)
        addressLine1 = models.CharField(null=True, blank=True, max_length=100)
        addressLine2 = models.CharField(null=True, blank=True, max_length=100)
        city = models.CharField(null=True, blank=True, max_length=100)
        province = models.CharField(null=True, blank=True, max_length=100)
        country = models.CharField(null=True, blank=True, max_length=100)
        postalCode = models.CharField(null=True, blank=True, max_length=100)
        profileImage = ResizedImageField(size=[200, 200], quality=90, upload_to='profile_images')
      
        monthlyCount = models.CharField( null=True, blank=True, max_length=100)
        subscribed = models.BooleanField(default=False)
        subscriptionType = models.CharField(choices=SUBSCRIPTION_OPTIONS,default='free', max_length=100)
        subscriptionReference = models.CharField( null=True, blank=True, max_length=100)
        
       

        uniqueId = models.CharField(null=True, blank=True, max_length=100)
        slug = models.SlugField(max_length=250, unique=True, blank=True, null=True)
        date_created = models.DateTimeField(blank=True, null=True)
        last_updated = models.DateTimeField(blank=True, null=True)
        
      
	       

        def __str__(self):
            return  '{} {} {} '.format(self.user.first_name, self.user.last_name, self.user.email)
    





        def save(self, *args, **kwargs):
            if self.date_created is None:
                self.date_created = timezone.localtime(timezone.now())
            if self.uniqueId is None:
                self.uniqueId = str(uuid4()).split('-')[4]
            # self.slug = slugify('{} {} {} '.format(self.user.first_name, self.user.last_name, self.user.email))


            self.slug = slugify('{} {} {} '.format(self.user.first_name, self.user.last_name, self.user.email))
            self.last_updated = timezone.localtime(timezone.now())
            super(Profile, self).save(*args, **kwargs)
        
        
        
class Blog(models.Model):
        title  =  models.CharField( max_length=200)
        blogIdea  =  models.CharField( null=True, blank=True,max_length=200)
        keywords=  models.CharField(null=True, blank=True, max_length=300)
        audience= models.CharField(null=True, blank=True, max_length=100)
        wordCount=  models.CharField(null=True, blank=True, max_length=200)
            
        #related fields
        profile = models.ForeignKey(Profile,default = "", on_delete=models.CASCADE)
        uniqueId = models.CharField(null=True, blank=True, max_length=100)
        slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
        date_created = models.DateTimeField(blank=True, null=True)
        last_updated = models.DateTimeField(blank=True, null=True)
  #Utility variable           
# uniqueId = models.CharField(null=True, blank=True, max_length=100)
# slug = models.SlugField(max_length=1000, unique=True, blank=True, null=True)
# date_created = models.DateTimeField(blank=True, null=True)
# last_updated = models.DateTimeField(blank=True, null=True)

        def __str__(self):
            return  '{} {}'.format(self.title, self.uniqueId)


       

        def save(self, *args, **kwargs):
            if self.date_created is None:
                self.date_created = timezone.localtime(timezone.now())
            if self.uniqueId is None:
                self.uniqueId = str(uuid4()).split('-')[4]
            # self.slug = slugify('{} {} {} '.format(self.user.first_name, self.user.last_name, self.user.email))


            self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
            self.last_updated = timezone.localtime(timezone.now())
            super(Blog, self).save(*args, **kwargs)
        
        
       
class BlogSection(models.Model):
        title  =  models.CharField( max_length=200)
        body  =  models.TextField(null=True, blank=True)
        wordCount=  models.CharField(null=True, blank=True, max_length=200)

            # profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
        blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
            
             
        uniqueId = models.CharField(null=True, blank=True, max_length=100)
        slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
        date_created = models.DateTimeField(blank=True, null=True)
        last_updated = models.DateTimeField(blank=True, null=True)

        def __str__(self):
            return  '{} {}'.format(self.title, self.uniqueId)
 



        def save(self, *args, **kwargs):
            if self.date_created is None:
                self.date_created = timezone.localtime(timezone.now())
            if self.uniqueId is None:
                self.uniqueId = str(uuid4()).split('-')[4]
                        # self.slug = slugify('{} {} {} '.format(self.user.first_name, self.user.last_name, self.user.email))


            self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
            self.last_updated = timezone.localtime(timezone.now())
                ###Couunt the words
            if self.body:
                x = len(self.body.split(' '))
                self.wordCount = str(x)
                    
            super(BlogSection, self).save(*args, **kwargs)