from django.shortcuts import render ,redirect,get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect


from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from django.core.files.base import ContentFile
from dashboard.models import Image
from django.conf import settings
from django.views.generic.base import TemplateView

import datetime
from datetime import timedelta
from datetime import datetime as dt
import requests
import json



from .forms import *
from .models import *
from .functions import *
import time 


# importing the openai API
import openai



# import stripe
# stripe.api_key = settings.STRIPE_SECRET_KEY




openai.api_key = settings.OPENAI_API_KEYS

from django.core.mail import send_mail, BadHeaderError,EmailMessage
from .forms import ContactForm

def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ["easir956@gmail.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")
    return render(request, "dashboard/email.html", {"form": form})

def successView(request):
    
    return HttpResponse("Success! Thank you for your message.")





@login_required
def lpg(request):
    context = {}
    if request.method =='POST':
        businessName = request.POST['businessName']
        businessDo = request.POST['businessDo']
        
        
        context ['section1Title'] = returnSection1Title(businessDo)
        context['section1Description'] = returnSection1Description(businessName,businessDo)
        
         
        #Get the service titles
        services = []
        serviceTitles =return3Services(businessDo)
        for service in serviceTitles:
            obj = {}
            serviceDescription = returnServiceDescription(service)
            obj['title'] = service 
            obj['description'] = serviceDescription
            services.append(obj)
            time.sleep (1)
            
        
        
        #Get the features titles
            
        features = []
        featureTitles = return3Features (businessDo)
        for feature in featureTitles:
            obj = {}
            featureDescription = returnFeatureDescription(features)
            obj['title'] = feature 
            obj['description'] = featureDescription
            features.append(obj) 
            time.sleep (1)
            
            
            
         
         
         
        context['service1Title']  = services [0]['title']
        context['service1Description'] = services [0]['description']
        context['service2Title']  = services [0]['title']
        context['service2Description'] = services [0]['description']
        context['service3Title'] = services [0]['title']
        context['service3Description'] = services [0]['description']
        
        
        context['section3Title'] = returnSection1Title(businessDo)
        context['section3Description'] = returnSection1Description(businessName,businessDo)
        
        context['features1Title'] = features[0]['title']
        context['features1Description'] = features[0]['description']
        context['features2Title'] = features[0]['title']
        context['features2Description'] = features[0]['description']
        context['features3Title'] = features[0]['title']
        context['features3Description'] = features[0]['description']
  
        
        return render (request,'dashboard/ai-website.html', context)
        
    return render (request,'dashboard/lpg.html', context)
    
@login_required
def website(request):
   context = {}
   
        
   return render (request,'dashboard/website.html', context)    
    
    
    
    
@login_required
def home(request):
    
    emptyBlogs = []
    completedBlogs= []
    monthCount = 0
    blogs=Blog.objects.filter(profile=request.user.profile)
    for blog in blogs:     
        sections = BlogSection.objects.filter(blog=blog)
        if sections.exists():
            blogWords = 0
            for section in sections:
              if section.wordCount:  
                blogWords += int(section.wordCount)
                monthCount = str(section.wordCount)
                
            blog.wordCount = str(blogWords)
            blog.monthlyCount = str(monthCount)
            blog.save()
            completedBlogs.append(blog)
        else:
            emptyBlogs.append(blog)
           
    context = {}
    context ['numBlogs'] = len(completedBlogs)
    context ['monthCount'] =request.user.profile.monthlyCount  
    context ['countReset'] =  '23rd-july ,2023 '                 
    # context ['countReset'] =getNextSubscriptionDate(request.user.profile)
    context ['emptyBlogs'] =emptyBlogs     
    context ['completedBlogs'] =completedBlogs 
    context ['allowance'] = checkCountAllowance(request.user.profile) 
    
    
   

     
        
    return render (request,'dashboard/home.html', context)





def index(request):
	user_membership = UserMembership.objects.get(user=request.user)
	subscriptions = Subscription.objects.filter(user_membership=user_membership).exists()
	if subscriptions == False:
		return redirect('sub')
	else:
		subscription = Subscription.objects.filter(user_membership=user_membership).last()
		return render(request, 'dashboard/home.html', {'sub': subscription})





def subscription(request):
	return render(request, 'dashboard/subscription.html')

def end_sub(request):
	return render(request, 'sub.html')

def subscribe(request):
	plan = request.GET.get('sub_plan')
	fetch_membership = Membership.objects.filter(membership_type=plan).exists()
	if fetch_membership == False:
		return redirect('subscribe')
	membership = Membership.objects.get(membership_type=plan)
	price = float(membership.price)*100 # We need to multiply the price by 100 because Paystack receives in kobo and not naira.
	price = int(price)

	def init_payment(request):
		url = 'https://www.paypal.com/sdk/js?client-id=AUv8rrc_P-EbP2E0mpb49BV7rFt3Usr-vdUZO8VGOnjRehGHBXkSzchr37SYF2GNdQFYSp72jh5QUhzG&vault=true&intent=subscription'
		headers = {
			'Authorization': 'Bearer '+settings.PAYPAL_SECRET,
			'Content-Type' : 'application/json',
			'Accept': 'application/json',
			}
		datum = {
			"email": request.user.email,
			"amount": price
			}
		x = requests.post(url, data=json.dumps(datum), headers=headers)
		if x.status_code != 200:
			return str(x.status_code)
		
		results = x.json()
		return results
	initialized = init_payment(request)
	print(initialized['data']['authorization_url'])
	amount = price/100
	instance = PayHistory.objects.create(amount=amount, payment_for=membership, user=request.user, paystack_charge_id=initialized['data']['reference'], paystack_access_code=initialized['data']['access_code'])
	UserMembership.objects.filter(user=instance.user).update(reference_code=initialized['data']['reference'])
	link = initialized['data']['authorization_url']
	return HttpResponseRedirect(link)
# return render(request, 'dashboard/subscribe.html')

def call_back_url(request):
	reference = request.GET.get('reference')
	# We need to fetch the reference from PAYMENT
	check_pay = PayHistory.objects.filter(paystack_charge_id=reference).exists()
	if check_pay == False:
		# This means payment was not made error should be thrown here...
		print("Error")
	else:
		payment = PayHistory.objects.get(paystack_charge_id=reference)
		# We need to fetch this to verify if the payment was successful.
		def verify_payment(request):
			url = 'https://www.paypal.com/sdk/js?client-id=AUv8rrc_P-EbP2E0mpb49BV7rFt3Usr-vdUZO8VGOnjRehGHBXkSzchr37SYF2GNdQFYSp72jh5QUhzG&vault=true&intent=subscription'+reference
			headers = {
				'Authorization': 'Bearer '+settings.PPAYPAL_SECRET,
				'Content-Type' : 'application/json',
				'Accept': 'application/json',
				}
			datum = {
				"reference": payment.paystack_charge_id
				}
			x = requests.get(url, data=json.dumps(datum), headers=headers)
			if x.status_code != 200:
				return str(x.status_code)
			
			results = x.json()
			return results
	initialized = verify_payment(request)
	if initialized['data']['status'] == 'success':
		PayHistory.objects.filter(paystack_charge_id=initialized['data']['reference']).update(paid=True)
		new_payment = PayHistory.objects.get(paystack_charge_id=initialized['data']['reference'])
		instance = Membership.objects.get(id=new_payment.payment_for.id)
		sub = UserMembership.objects.filter(reference_code=initialized['data']['reference']).update(membership=instance)
		user_membership = UserMembership.objects.get(reference_code=initialized['data']['reference'])
		Subscription.objects.create(user_membership=user_membership, expires_in=dt.now().date() + timedelta(days=user_membership.membership.duration))
		return redirect('subscribed')
	return render(request, 'dashboard/payment.html')


def subscribed(request):
	return render(request, 'dashboard/subscribed.html')



@login_required
def profile(request,*args, **kwargs):
    context = {}                      
                                  
    if request.method == 'GET':
        form  = ProfileForm(instance=request.user.profile,user=request.user)
        image_form =ProfileImageForm(instance=request.user.profile)
                                 
        context ['form'] =form                          
        context ['image_form'] =image_form
        return render(request, 'dashboard/profile.html', context)
    
    
    if request.method == 'POST':
        
        form = ProfileForm(request.POST ,instance=request.user.profile, user=request.user)
        image_form  = ProfileImageForm(request.POST,request.FILES,instance=request.user.profile)
       
        if form.is_valid():
           form.save()
           return redirect('profile') 
    
        if image_form.is_valid():
            image_form.save()
            return redirect('profile')
   
    return render(request, 'dashboard/profile.html', context)












@login_required
def generate_image_from_text(request):
    context={} 
    object = None
    if settings.OPENAI_API_KEYS is not None and request.method == 'POST':
        
        web = request.POST.get('web')
        
        # Call the OpenAI API to translate the input
        
        response = openai.Image.create(
            
            prompt= web,
            n=1,
            size = '256x256' # 512x512 1024x1024
            )
        print(response)
        img_url = response["data"][0]["url"]
        response = requests.get(img_url)
        img_file = ContentFile(response.content)
        count = Image.objects.count() +1
        fname = f"image-{count}.jpg"
        obj = Image(phrase = web)
        obj.ai_image.save (fname, img_file)
        obj.save()
        print(obj)
        
        
    return render(request, 'dashboard/images.html', context) 




@csrf_exempt
def P_translate(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt', '')
        
        # Call the OpenAI API to translate the input
        
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["###"]
        )
        
        result = response.choices[0].text
        return render(request, 'dashboard/ptranslate.html', {'result': result})
    else:
        return render(request, 'dashboard/ptranslate.html')
       
    

 
 
 

@login_required
def webTopic(request):
  context={}
  if request.method == 'POST':
      #retriving the blogIdea String from thr submitted Form which comes in the request.POST
    
    # webIdea = request.POST['webIdea']
    # request.session['webIdea']=webIdea
    web = request.POST['web']
    #SAVING THAT blogIdea in the session to access later in another route for example
    request.session['web']=web
    webTopics = generateWebTopicIdeas(web)
    if len(webTopics)>0:
        request.session['webTopics'] = webTopics
        pass
        return redirect('web-sections')
    else:
    
        messages.error(request, 'Sorry We could not able to generate any idea for you , please try again')
        return redirect('web-topic')

    
  return render(request, 'dashboard/web-topic.html', context)  






@login_required
def webSections(request):
    
    if 'webTopics' in request.session:
        pass
            
    else:
            messages.error(request, "start by creating web topic Ideas")
            return redirect('web-topic')
    context={} 
    context['webTopics'] =  request.session['webTopics']
    return render(request, 'dashboard/web-sections.html', context) 




@login_required   
def createWebFromTopic(request,uniqueId):
    context = {}
    try:
        web = Web.object.get(uniqueId= uniqueId)
    except:
        messages.error(request, "Web not found")
        return redirect ('dashboard')
    
    webSections = generateWebSectionTitles(web.title,web.web)
    
    if len (webSections)>0:
        #adding the sections to the session
        request.session ['webSections'] = webSections
        #adding the sections to the context
        
        context ['webSections'] = webSections
        # context ['slug'] = blog.slug
        
        # return redirect ('select-blog-sections')
    else: 
        messages.error(request, "not possible from AI system , Please try again later")
        return redirect ('web-topic')
    
    
    if request.method == 'POST':
        for val in request.POST:
            if not 'csrfmiddlewaretoken' in val :
                prevWev= ''
                wSections = WebSection.objects.filter(web= web).order_by('date_created')
                for sec in wSections:
                    prevWev = sec.title + '\n'
                    prevWev += sec.body.replace('<br>','\n')
                prevWev = ''
                section = generateWebSectionDetails(web.title,val,web.web,prevWev,request.user.profile)
                # Create database record
                webSec = WebSection.objects.create(
                title= val,
                body = section,
                web =web)    
                webSec.save()
                time.sleep(2)
            wSections = WebSection.objects.filter(web= web)
            context = {}
            context ['web'] = web
            context ['webSections'] = webSections
        
            return redirect ('view-generated-web', slug=web.slug)
        
        return render (request , 'dashboard/select-blog-sections.html', context)


@login_required   
def rewriteWeb(request,uniqueId):
    
    try:
        web = Web.object.get(uniqueId= uniqueId)
    except:
        messages.error(request, "Web not found")
        return redirect ('dashboard')
    
    titles = []
    webSections = WebSection.objects.filter(web= web).order_by('date_created')
    for section in webSections:
        titles.append(section.title)
        section.delete()
    for val in titles:
        prevWeb= ''
        wSections = WebSection.objects.filter(web= web).order_by('date_created')
        for sec in wSections:
            prevWeb = sec.title + '\n'
            prevWeb += sec.body.replace('<br>','\n')
        prevWeb = ''
        section = generateWebSectionDetails(web.title,val,web.web, web.keywords,prevWeb,request.user.profile)
        # Create database record
        webSec = WebSection.objects.create(
        title= val,
        body = section,
        web = web)    
        webSec.save()
        time.sleep(5)
        
    wSections = WebSection.objects.filter( web=  web)
    context = {}
    context [' web'] =  web
    context [' webSections'] =  webSections
    
        # return redirect ('view-generated-blog', slug=blog.slug)
        
    return render (request , 'dashboard/view-generated-web.html', context)



@login_required  
def viewGeneratedWeb(request, slug):
    try:
        web = Web.objects.get(slug=slug)
    except:
        
        messages.error(request, " Please try again later")
        return redirect ('blog-topic')
    # fetch the created section for the blog
    webSections = WebSection.objects.filter(web= web)
    context = {}
    context ['web'] = web
    context ['webSections'] = webSections
    
    return render (request , 'dashboard/view-generated-web.html', context)
    
  



@login_required  
def deleteWebTopic (request,uniqueId):
    try: 
        web= Web.objects.get(uniqueId= uniqueId)
        if web.profile == request.user.profile:
            web.delete()
            return redirect ('dashboard')
        else:
            messages.error(request, "Access denied")
            return redirect ('dashboard')
    except:
            messages.error(request, "Blog not found this time , Please try again later")
            return redirect ('dashboard')
        
@login_required
def saveWebTopic(request,webTopic):
    if 'webIdea' in request.session and 'web' in request.session and 'webTopics'  in request.session:
    
            web=Web.objects.create(
            title  = webTopic,
            # webIdea  = request.session['webIdea'],
            web= request.session['web'],
            profile = request.user.profile)
            web.save()
            webTopics =  request.session['webTopics']
            webTopics.remove(webTopic)
            request.session['webTopics'] = webTopics
            return redirect('web-sections')
            
    else:
            return redirect('web-topic')

            
        
@login_required   
def useWebTopic(request,webTopic):
    context = {}
    if  'web' in request.session and 'webTopics'  in request.session:
       
       if Web.objects.filter(title =webTopic).exists():
           web = Web.objects.get(title =webTopic)
       else: 
           #start by saving blog ...
                web= Web.objects.create(
                title  = webTopic,
                # webIdea  = request.session['webIdea'],
                web= request.session['web'],
                profile = request.user.profile)
                web.save()
       webSections = generateWebSectionTitles(webTopic,request.session['web'])
        
    else:
        return redirect('web-topic')
    if request.method == 'POST':
        for val in request.POST:
            if not 'csrfmiddlewaretoken' in val :
                prevWeb= ''
                wSections = WebSection.objects.filter(web=web).order_by('date_created')
                for sec in wSections:
                    prevWeb += sec.title + '\n'
                    prevWeb += sec.body.replace('<br>','\n')
                prevWeb = ''   
                section = generateWebSectionDetails(webTopic,val, request.session['web'] , prevWeb,request.user.profile)
                # Create database record
                webSec = WebSection.objects.create(
                title= val,
                body = section,
                web =web)
                webSec.save()
                time.sleep(2)
        return redirect ('view-generated-web', slug=web.slug)
    
    
            
            
            
    if len (webSections)>0:
        #adding the sections to the session
        request.session ['webSections'] = webSections
        #adding the sections to the context
        
        context ['webSections'] = webSections
        # context ['slug'] = blog.slug
        
        # return redirect ('select-blog-sections')
    else: 
        messages.error(request, "not possible from AI system , Please try again later")
        return redirect ('web-topic')
    
    
    
        
    return render (request , 'dashboard/select-web-sections.html', context)



#####################################





@login_required
def blogTopic(request):
  context={}
  if request.method == 'POST':
      #retriving the blogIdea String from thr submitted Form which comes in the request.POST

    blogIdea = request.POST['blogIdea']
    #SAVING THAT blogIdea in the session to access later in another route for example
    request.session['blogIdea']=blogIdea
    keywords = request.POST['keywords']
    request.session['keywords']=keywords
    audience = request.POST['audience']
    request.session['audience']=audience


    blogTopics = generateBlogTopicIdeas (blogIdea,audience,keywords)
    if len(blogTopics)>0:
        request.session['blogTopics'] = blogTopics
        return redirect('blog-sections')
    else:
    
        messages.error(request, 'Sorry We could not able to generate any idea for you , please try again')
        return redirect('blog-topic')

    
  return render(request, 'dashboard/blog-topic.html', context)  

@login_required
def blogSections(request):
    
    if 'blogTopics' in request.session:
        pass
            
    else:
            messages.error(request, "start by creating blog topic Ideas")
            return redirect('blog-topic')
    context={} 
    context['blogTopics'] =  request.session['blogTopics']
    return render(request, 'dashboard/blog-sections.html', context) 


@login_required  
def deleteBlogTopic (request,uniqueId):
    try: 
        blog= Blog.objects.get(uniqueId= uniqueId)
        if blog.profile == request.user.profile:
            blog.delete()
            return redirect ('dashboard')
        else:
            messages.error(request, "Access denied")
            return redirect ('dashboard')
    except:
            messages.error(request, "Blog not found this time , Please try again later")
            return redirect ('dashboard')
        
@login_required
def saveBlogTopic(request,blogTopic):
    if 'blogIdea' in request.session and 'keywords' in request.session and'audience' in request.session and 'blogTopics'  in request.session:
    
            blog=Blog.objects.create(
            title  = blogTopic,
            blogIdea  = request.session['blogIdea'],
            keywords= request.session['keywords'],
            audience= request.session['audience'],
            profile = request.user.profile)
            blog.save()
            blogTopics =  request.session['blogTopics']
            blogTopics.remove(blogTopic)
            request.session['blogTopics'] = blogTopics
            return redirect('blog-sections')
            
    else:
            return redirect('blog-topic')

 


            
        
@login_required   
def useBlogTopic(request,blogTopic):
    context = {}
    if 'blogIdea' in request.session and 'keywords' in request.session and'audience' in request.session :
       
       if Blog.objects.filter(title =blogTopic).exists():
           blog = Blog.objects.get(title =blogTopic)
       else: 
           #start by saving blog ...
            blog=Blog.objects.create(
            title  = blogTopic,
            blogIdea  = request.session['blogIdea'],
            keywords= request.session['keywords'],  
            audience= request.session['audience'],
            profile = request.user.profile)
            blog.save()
       blogSections = generateBlogSectionTitles(blogTopic,request.session['audience'],request.session['keywords'])
        
    else:
        return redirect('blog-topic')
    if request.method == 'POST':
        for val in request.POST:
            if not 'csrfmiddlewaretoken' in val :
                prevBlog= ''
                bSections = BlogSection.objects.filter(blog=blog).order_by('date_created')
                for sec in bSections:
                    prevBlog += sec.title + '\n'
                    prevBlog += sec.body.replace('<br>','\n')
                prevBlog = ''   
                section = generateBlogSectionDetails(blogTopic,val, request.session['audience'] ,request.session ['keywords'] ,prevBlog,request.user.profile)
                # Create database record
                blogSec = BlogSection.objects.create(
                title= val,
                body = section,
                blog =blog)
                blogSec.save()
                time.sleep(2)
        return redirect ('view-generated-blog', slug=blog.slug)
    
    
            
            
            
    if len (blogSections)>0:
        #adding the sections to the session
        request.session ['blogSections'] = blogSections
        #adding the sections to the context
        
        context ['blogSections'] = blogSections
        # context ['slug'] = blog.slug
        
        # return redirect ('select-blog-sections')
    else: 
        messages.error(request, "not possible from AI system , Please try again later")
        return redirect ('blog-topic')
    
    
    
        
    return render (request , 'dashboard/select-blog-sections.html', context)








           
@login_required   
def createBlogFromTopic(request,uniqueId):
    context = {}
    try:
        blog = Blog.object.get(uniqueId= uniqueId)
    except:
        messages.error(request, "Blog not found")
        return redirect ('dashboard')
    
    blogSections = generateBlogSectionTitles(blog.title,blog.audience,blog.keywords)
    
    if len (blogSections)>0:
        #adding the sections to the session
        request.session ['blogSections'] = blogSections
        #adding the sections to the context
        
        context ['blogSections'] = blogSections
        # context ['slug'] = blog.slug
        
        # return redirect ('select-blog-sections')
    else: 
        messages.error(request, "not possible from AI system , Please try again later")
        return redirect ('blog-topic')
    
    
    if request.method == 'POST':
        for val in request.POST:
            if not 'csrfmiddlewaretoken' in val :
                prevBlog= ''
                bSections = BlogSection.objects.filter(blog= blog).order_by('date_created')
                for sec in bSections:
                    prevBlog = sec.title + '\n'
                    prevBlog += sec.body.replace('<br>','\n')
                prevBlog = ''
                section = generateBlogSectionDetails(blog.title,val,blog.audience,blog.keywords,prevBlog,request.user.profile)
                # Create database record
                blogSec = BlogSection.objects.create(
                title= val,
                body = section,
                blog =blog)    
                blogSec.save()
                time.sleep(2)
            bSections = BlogSection.objects.filter(blog= blog)
            context = {}
            context ['blog'] = blog
            context ['blogSections'] = blogSections
        
            return redirect ('view-generated-blog', slug=blog.slug)
        
        return render (request , 'dashboard/select-blog-sections.html', context)








            
@login_required   
def rewriteBlog(request,uniqueId):
    
    try:
        blog = Blog.object.get(uniqueId= uniqueId)
    except:
        messages.error(request, "Blog not found")
        return redirect ('dashboard')
    
    titles = []
    blogSections = BlogSection.objects.filter(blog= blog).order_by('date_created')
    for section in blogSections:
        titles.append(section.title)
        section.delete()
    for val in titles:
        prevBlog= ''
        bSections = BlogSection.objects.filter(blog= blog).order_by('date_created')
        for sec in bSections:
            prevBlog = sec.title + '\n'
            prevBlog += sec.body.replace('<br>','\n')
        prevBlog = ''
        section = generateBlogSectionDetails(blog.title,val,blog.audience,blog.keywords,prevBlog,request.user.profile)
        # Create database record
        blogSec = BlogSection.objects.create(
        title= val,
        body = section,
        blog =blog)    
        blogSec.save()
        time.sleep(5)
        
    bSections = BlogSection.objects.filter(blog= blog)
    context = {}
    context ['blog'] = blog
    context ['blogSections'] = blogSections
    
        # return redirect ('view-generated-blog', slug=blog.slug)
        
    return render (request , 'dashboard/view-generated-blog.html', context)



@login_required  
def viewGeneratedBlog(request, slug):
    try:
        blog = Blog.objects.get(slug=slug)
    except:
        
        messages.error(request, " Please try again later")
        return redirect ('blog-topic')
    # fetch the created section for the blog
    blogSections = BlogSection.objects.filter(blog= blog)
    context = {}
    context ['blog'] = blog
    context ['blogSections'] = blogSections
    
    return render (request , 'dashboard/view-generated-blog.html', context)
    
  
  
 
@login_required  
def billing(request):
    context = {}  
    return render (request , 'dashboard/billing.html', context)
  
@require_POST 
@csrf_exempt
def webhook(request):
     return redirect ('billing')  
        
@login_required
def PaypalPaymentSuccess(request):
    if request.POST['type'] == 'starter':
        try:
            profile = Profile.objects.get(uniqueID = request.POST['userId'])
            profile.subscribed= True
            profile.subscriptionType= 'Starter'
            profile.subscriptionReference= request.POST['subscriptionID']
            profile.save()
            
        except:
            return JsonResponse({'result':'FAIL'})
    
    elif request.POST['type'] == 'advanced': 
        try:
            profile = Profile.objects.get(uniqueID = request.POST['userId'])
            profile.subscribed= True
            profile.subscriptionType= 'advanced'
            profile.subscriptionReference= request.POST['subscriptionID']
            profile.save()
            
        except:
            return JsonResponse({'result':'FAIL'})
    else:
        return JsonResponse({'result':'FAIL'})
        
    
    #  return redirect (billing)         
        
        

# @login_required(login_url='login')
# def profile(request):
#     context = {}  
#     if request.method == "POST":
#         form = ProfileForm(request.POST , request.FILES, instance=request.user.profile, user=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, ('Your profile was successfully created!!'))
#         else:
#             messages.error(request, 'Error saving form')

#         return redirect("profile")
    
#     # else:
#     #     user = request.user
#     #     profile = user.profile
#     #     form = ProfileForm(instance=profile)

#     # context = {'form' : form}
#     return render(request , 'dashboard/profile.html' , context)









#########################################################




@login_required
def NL_TO_API(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/results.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/NL to ChalkrAI API.html')







#########################################################



@login_required
def NL_TO_SAPI(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/striperesults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/NL to Stripe API.html')





#########################################################


 
def query(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        
        
        # Call the OpenAI API to translate the input
        
        response = openai.Completion.create(
          model="text-davinci-003",
          prompt=prompt,
          temperature=0,
          max_tokens=150,
          top_p=1.0,
          frequency_penalty=0.0,
          presence_penalty=0.0,
          stop=["#", ";"]
        )
        result = response.choices[0].text
        return render(request, 'dashboard/query.html', {'result': result})
    else:
        return render(request, 'dashboard/query.html')
 
 
#########################################################


@login_required
def PL_To_NL(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/nresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/Python to natural language.html')



#########################################################


@login_required
def C_T_C(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/Complexity.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/ctc.html')




#########################################################


@login_required
def T_P_L(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/tplresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/tpl.html')



#########################################################


@login_required
def E_C(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/ecresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/ec.html')




#########################################################


@login_required
def P_B_F(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/pbfresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/pbf.html')




#########################################################


@login_required
def J_H_C(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/pbfresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/jhc.html')


#########################################################


@login_required
def J_T_P(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/jtpresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/jtp.html')


#########################################################


@login_required
def W_P_D(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/wpdresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/wpd.html')



#########################################################


@login_required
def J_O_L_F(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/jolfresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/jolf.html')


#########################################################


@login_required
def Q_A(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/qaresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/qa.html')




#########################################################


@login_required
def G_C(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/gcresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/gc.html')



#########################################################


@login_required
def Summarize(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/sf2gresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/sf2g.html')


#########################################################


@login_required
def T_C(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/ttcresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/ttc.html')



#########################################################


@login_required
def E_Translate(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/etolresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/etol.html')



#########################################################


@login_required
def Parse_unstructured_data(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/pudresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/pud.html')

#########################################################


@login_required
def Movie_to_Emoji(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/mteresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/mte.html')

#########################################################

@login_required
def Factual_Answering(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/faresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/fa.html')


#########################################################

@login_required
def Ad_From_Product_Description(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/afpdresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/afpd.html')


#########################################################

@login_required
def Product_Name_Generator(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/pngresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/png.html')


#########################################################

@login_required
def TL_DR_Summarization(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/tldrresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/tldr.html')


#########################################################

@login_required
def Spreadsheet_Creator(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/scrresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/sc.html')


#########################################################

@login_required
def ML_AI_Language_Model_Tutor(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/mlairesults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/mlai.html')


#########################################################

@login_required
def Science_Fiction_Book_List_Maker(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/sfblmresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/sfblm.html')



#########################################################

@login_required
def Airport_Code_Extractor(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/aceresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/ace.html')



#########################################################

@login_required
def SQL_Request(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/srresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/sr.html')




#########################################################

@login_required
def Extract_Contact_Information(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/eciresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/eci.html')



#########################################################

@login_required
def Friend_chat(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/fcresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/fc.html')


#########################################################

@login_required
def Mood_To_Color(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/mtcresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/mtc.html')




   
   
   #########################################################

@login_required
def Analogy_Maker(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/amresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/am.html')



#########################################################

@login_required
def Micro_Horror_Story_Creator(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/mhscresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/mhsc.html')



#########################################################

@login_required
def Third_Person_Converter(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/tpcresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/tpc.html')




#########################################################

@login_required
def Notes_To_Summary(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/ntcresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/ntc.html')




#########################################################

@login_required
def VR_Fitness_Idea_Generator(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/vfigresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/vfig.html')




#########################################################

@login_required
def Essay_Outline(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/eoresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/eo.html')





#########################################################

@login_required
def Recipe_Creator(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/rcresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/rc.html')





#########################################################

@login_required
def Chat(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/chatresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/chat.html')



#########################################################

@login_required
def Marv_Sarcastic_Chat_Bot(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/mscbresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/mscb.html')



#########################################################

@login_required
def Turn_By_Turn_Directions(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/ttdresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/ttd.html')





#########################################################

@login_required
def Restaurant_Review_Creator(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/rrcresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/rrc.html')



#########################################################

@login_required
def Create_Study_Sotes(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/csnresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/csn.html')



#########################################################

@login_required
def Interview_Questions(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/iqresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/iq.html')





#########################################################

@login_required
def Keywords(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/keywordsresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/keywords.html')




#########################################################

@login_required
def Classification(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/classificationresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/classification.html')


#########################################################

@login_required
def Advanced_Tweet_Classifier(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/advancedtweetclassifierresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/advancedtweetclassifier.html')



#########################################################

@login_required
def Tweet_Classifier(request):
    if request.method == 'POST':
        # Get the user input from the form
        prompt = request.POST['prompt']

        # Call the OpenAI API to translate the input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        # Extract the translations from the response
        translations = response.choices[0].text.split('\n')

        # Render the results template with the translations
        return render(request, 'dashboard/tweetresults.html', {'translations': translations})

    # Render the translation form template
    return render(request, 'dashboard/tweet.html')









