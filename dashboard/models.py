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
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.conf import settings


import datetime
from datetime import timedelta
from datetime import datetime as dt


today = datetime.date.today()
















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
            
            
            
            
            
            
#### User Payment History
class PayHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    paystack_charge_id = models.CharField(max_length=100, default='', blank=True)
    paystack_access_code = models.CharField(max_length=100, default='', blank=True)
    payment_for = models.ForeignKey('Membership', on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    paid = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

#### Membership
class Membership(models.Model):
    MEMBERSHIP_CHOICES = (
    	('Extended', 'Extended'), # Note that they are all capitalize//
    	('Advanced', 'Advanced'),
    	('Medium', 'Medium'),
        ('Basic', 'Basic'),
        ('Free', 'Free')
    )
    PERIOD_DURATION = (
        ('Days', 'Days'),
        ('Week', 'Week'),
        ('Months', 'Months'),
    )
    slug = models.SlugField(null=True, blank=True)
    membership_type = models.CharField(choices=MEMBERSHIP_CHOICES, default='Free', max_length=30)
    duration = models.PositiveIntegerField(default=7)
    duration_period = models.CharField(max_length=100, default='Day', choices=PERIOD_DURATION)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
       return self.membership_type

#### User Membership
class UserMembership(models.Model):
    user = models.OneToOneField(User, related_name='user_membership', on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, related_name='user_membership', on_delete=models.SET_NULL, null=True)
    reference_code = models.CharField(max_length=100, default='', blank=True)

    def __str__(self):
       return self.user.username

@receiver(post_save, sender=UserMembership)
def create_subscription(sender, instance, *args, **kwargs):
	if instance:
		Subscription.objects.create(user_membership=instance, expires_in=dt.now().date() + timedelta(days=instance.membership.duration))


#### User Subscription
class Subscription(models.Model):
    user_membership = models.ForeignKey(UserMembership, related_name='subscription', on_delete=models.CASCADE, default=None)
    expires_in = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
      return self.user_membership.user.username

@receiver(post_save, sender=Subscription)
def update_active(sender, instance, *args, **kwargs):
	if instance.expires_in < today:
		subscription = Subscription.objects.get(id=instance.id)
		subscription.delete()      
  
  
  
  

# class StripeCustomer(models.Model):
#     user = models.OneToOneField(to=User, on_delete=models.CASCADE)
#     stripeCustomerId = models.CharField(max_length=255)
#     stripeSubscriptionId = models.CharField(max_length=255)

#     def __str__(self):
#         return self.user.username



class StripeSubscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="subscriptions")
    active = models.BooleanField(default=False)
    stripe_subscription = models.CharField(max_length=100,blank=True,
        help_text = "The user's Stripe Customer object, if it exists")
    last4 = models.CharField(max_length=4,blank=True,
        help_text = "The user's last 4 credit card digits, if they exist")

    def __str__(self):
        return str(self.user)