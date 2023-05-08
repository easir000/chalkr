from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone
from .utils import generate_ref_code

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
        bio = models.TextField(blank=True)
        code = models.CharField(max_length=12,blank=True)
        recommended_by = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='reff_by')
        
       

        uniqueId = models.CharField(null=True, blank=True, max_length=100)
        slug = models.SlugField(max_length=250, unique=True, blank=True, null=True)
        date_created = models.DateTimeField(blank=True, null=True,auto_now=True)
        last_updated = models.DateTimeField(blank=True, null=True,auto_now_add=True)
        
      
	       

        def __str__(self):
            return  '{} {} {} '.format(self.user.first_name, self.user.last_name, self.user.email,self.code)
    

        def get__recommended_profiles(self):
            qs = Profile.objects.all()



        def save(self, *args, **kwargs):
            if self.date_created is None:
                self.date_created = timezone.localtime(timezone.now())
            if self.uniqueId is None:
                self.uniqueId = str(uuid4()).split('-')[4]
            if self.code =="":
                code = generate_ref_code() 
                self.code = code
            # self.slug = slugify('{} {} {} '.format(self.user.first_name, self.user.last_name, self.user.email))


            self.slug = slugify('{} {} {} '.format(self.user.first_name, self.user.last_name, self.user.email,self.code))
            self.last_updated = timezone.localtime(timezone.now())
            super(Profile, self).save(*args, **kwargs)
        

class Image(models.Model):
        phrase  =  models.CharField( max_length=200)
        ai_image  =  models.ImageField( upload_to = 'images')
        

        def __str__(self):
            return  str(self.phrase)




class Web(models.Model):
        title  =  models.CharField( max_length=200)
       
        web= models.CharField(null=True, blank=True, max_length=100)
        wordCount=  models.CharField(null=True, blank=True, max_length=200)
            
        #related fields
        profile = models.ForeignKey(Profile,default = "", on_delete=models.CASCADE)
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
            super(Web, self).save(*args, **kwargs)



 
class WebSection(models.Model):
        title  =  models.CharField( max_length=200)
        body  =  models.TextField(null=True, blank=True)
        wordCount=  models.CharField(null=True, blank=True, max_length=200)

            # profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
        web = models.ForeignKey(Web, on_delete=models.CASCADE)
            
             
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
                    
            super(WebSection, self).save(*args, **kwargs)
 
 
 
 
 
 
       
        
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
            
            
            
            
            
            
            


class Lpg(models.Model):
        
       
        section1Title = models.CharField(null=True, blank=True, max_length=100)
        section1Description = models.TextField(null=True, blank=True)
        callToAction = models.CharField(null=True, blank=True, max_length=50)
        section1Image = models.ImageField(default= 'default.jpg', upload_to='landing_page_images')
        
        section3Title = models.CharField(null=True, blank=True, max_length=100)
        section3Description = models.TextField(null=True, blank=True)
        section3Image = models.ImageField(default= 'default.jpg', upload_to='landing_page_images')
        
        profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
        #related fields
        uniqueId = models.CharField(null=True, blank=True, max_length=100)
        slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
        date_created = models.DateTimeField(blank=True, null=True)
        last_updated = models.DateTimeField(blank=True, null=True)


        def __str__(self):
            return  '{} {}'. format(self.section1Title, self.uniqueId)


       

        def save(self, *args, **kwargs):
            if self.date_created is None:
                self.date_created = timezone.localtime(timezone.now())
            if self.uniqueId is None:
                self.uniqueId = str(uuid4()).split('-')[4]
            # self.slug = slugify('{} {} {} '.format(self.user.first_name, self.user.last_name, self.user.email))


            self.slug = slugify()
            self.last_updated = timezone.localtime(timezone.now())
            super(Lpg, self).save(*args, **kwargs)





class LpgService(models.Model):
        
       
        title = models.CharField(null=True, blank=True, max_length=200)
        description = models.TextField(null=True, blank=True)
        icon = models.CharField(null=True, blank=True, max_length=200)
        
        lpg = models.ForeignKey(Lpg,on_delete=models.CASCADE)
        profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
        
        #related fields
        uniqueId = models.CharField(null=True, blank=True, max_length=100)
        slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
        date_created = models.DateTimeField(blank=True, null=True)
        last_updated = models.DateTimeField(blank=True, null=True)


        def __str__(self):
            return  '{} {}'. format(self.title, self.uniqueId)



       

        def save(self, *args, **kwargs):
            if self.date_created is None:
                self.date_created = timezone.localtime(timezone.now())
            if self.uniqueId is None:
                self.uniqueId = str(uuid4()).split('-')[4]
            # self.slug = slugify('{} {} {} '.format(self.user.first_name, self.user.last_name, self.user.email))


            self.slug = slugify()
            self.last_updated = timezone.localtime(timezone.now())
            super(LpgService, self).save(*args, **kwargs)



class LpgFeatures(models.Model):
        
       
        title = models.CharField(null=True, blank=True, max_length=200)
        description = models.TextField(null=True, blank=True)
        icon = models.CharField(null=True, blank=True, max_length=200)
        image = models.ImageField(default='default.jpg',upload_to='landing_page_images')
        
        
        lpg = models.ForeignKey(Lpg,on_delete=models.CASCADE)
        profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
        
        #related fields
        uniqueId = models.CharField(null=True, blank=True, max_length=100)
        slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
        date_created = models.DateTimeField(blank=True, null=True)
        last_updated = models.DateTimeField(blank=True, null=True)


        def __str__(self):
            return  '{} {}'. format(self.title, self.uniqueId)



       

        def save(self, *args, **kwargs):
            if self.date_created is None:
                self.date_created = timezone.localtime(timezone.now())
            if self.uniqueId is None:
                self.uniqueId = str(uuid4()).split('-')[4]
            # self.slug = slugify('{} {} {} '.format(self.user.first_name, self.user.last_name, self.user.email))


            self.slug = slugify()
            self.last_updated = timezone.localtime(timezone.now())
            super(LpgFeatures, self).save(*args, **kwargs)