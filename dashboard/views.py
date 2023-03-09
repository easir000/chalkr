from django.shortcuts import render ,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import JsonResponse


from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt



from .forms import *
from .models import *
from .functions import *
import time 




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
    context ['countReset'] ='23/10/2023'
    context ['emptyBlogs'] =emptyBlogs     
    context ['completedBlogs'] =completedBlogs 
    context ['allowance'] = checkCountAllowance(request.user.profile)    
     
        
    return render (request,'dashboard/home.html', context)

@login_required
def profile(request):
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