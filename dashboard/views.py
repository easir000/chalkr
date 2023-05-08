from django.shortcuts import render ,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import JsonResponse


from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from django.core.files.base import ContentFile
from dashboard.models import Image
from django.conf import settings




from .forms import *
from .models import *
from .functions import *
import time 


# importing the openai API
import openai

openai.api_key = settings.OPENAI_API_KEYS


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
        profile_id =request.session.get('ref_profile')
        print('profile_id',profile_id)
        form = ProfileForm(request.POST ,instance=request.user.profile, user=request.user)
        image_form  = ProfileImageForm(request.POST,request.FILES,instance=request.user.profile)
       
       
       #Check if the form is valid or not  
        if form.is_valid():
            if profile_id is not None:
              recommended_by_profile = Profile.objects.get(id =profile_id)
              instance = form.save()
              registered_user= User.objects.get(id = instance.id)
              registered_profile=  Profile.objects.get(user = registered_user)
              registered_profile_recommended_by =  recommended_by_profile.user
              registered_profile.save()
              
        else:
           form.save()
           return redirect('profile') 
    
        if image_form.is_valid():
            image_form.save()
            return redirect('profile')

    code = str(kwargs.get('ref_code'))
    try:
       form = ProfileForm.objects.get(code=code)
       request.session['ref_form'] = form.id
       print('id','form.id')
    except:
        
        pass
    print(request.session.get_expiry_date())    
    
    return render(request, 'dashboard/profile.html', context)





@login_required
def translate(request):
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
    return render(request, 'dashboard/translate.html')






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
