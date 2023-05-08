import os
import openai
from django.conf import settings
import datetime
import json
import requests


from dateutil.relativedelta import relativedelta 
openai.api_key = settings.OPENAI_API_KEYS


def returnMonth(month):
  pass
  if month == 1:
    return 'January'
  elif month == 2:
    return 'February'
  elif month == 3:
    return 'March'
  elif month == 4:
    return 'April'
  elif month == 5:
    return 'May'
  elif month == 6:
    return 'June'
  elif month == 7:
    return 'July'
  elif month == 8:
    return 'August'
  elif month == 9:
    return 'September'
  elif month == 10:
    return 'October'
  elif month == 11:
    return 'November'
  else:
    return 'December'



def returnSection1Title(businessDo):
    
    
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Generate A website landing gpage title (only 5 words in the title) for the following business:\nWhat the business does:{} ".format(businessDo),
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )

    if 'choices' in response:
      if len(response['choices'])>0:
        answer = response['choices'] [0]['text'].replace('\n', '')
        return answer
             
      else:
         return ''
    else:
        return ''

def returnSection1Description(businessName,businessDo):

  response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Generate a website landing page paragraph description of 160 words for the following business:\nBusiness Name: {}\nWhat the business does:{}\n ".format(businessName,businessDo),
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)


  if 'choices' in response:
      if len(response['choices'])>0:
          answer = response['choices'] [0]['text'].replace('\n', '')
          return answer

         
      else:
         return ''
  else:
      return ''
  


def return3Services(businessDo):

  response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Generate A website landing gpage title of (only 5 words in the title) for the following business: What the business does:{}\n ".format(businessDo),
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)


  if 'choices' in response:
      if len(response['choices'])>0:
          answer = response['choices'] [0]['text'].replace('\n', '').replace('1', '').replace('2', '').replace('3', '')
          answer_list = answer.split(' . ')
          # answer_list.remove('')
          return answer_list

         
      else:
         return ''
  else:
      return ''
  

def returnServiceDescription(title):

  response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Generate a website landing page paragraph description of 160 words for the following business:\nBusiness Name: {}\n".format(title),
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)


  if 'choices' in response:
      if len(response['choices'])>0:
          answer = response['choices'] [0]['text'].replace('\n', '')
          return answer

         
      else:
         return ''
  else:
      return ''
  


def return3Features(businessDo):

  response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Generate A website landing gpage title of (only 5 words in the title) for the following business:\nWhat the business does:{} ".format(businessDo),
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)


  if 'choices' in response:
      if len(response['choices'])>0:
          answer = response['choices'] [0]['text'].replace('\n', '').replace('1', '').replace('2', '').replace('3', '')
          answer_list = answer.split(' . ')
          # answer_list.remove('')
          return answer_list

         
      else:
         return ''
  else:
      return ''
  



def returnFeatureDescription(title):

  response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Generate a website landing page paragraph description of 160 words for the following business:\nFeature Title: {}\n ".format(title),
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)


  if 'choices' in response:
      if len(response['choices'])>0:
          answer = response['choices'] [0]['text'].replace('\n', '')
          return answer

         
      else:
         return ''
  else:
      return ''
  





def generateWebTopicIdeas(web):
  web_topics = []
  
  # response = openai.Completion.create(
  # model="code-davinci-002",
  # prompt="##### Translate this function  from Python into Haskell\n### Python\n    \n    def predict_proba(X: Iterable[str]):\n        return np.array([predict_one_probas(tweet) for tweet in X])\n    \n### Haskell".format(web),
  # # prompt="Generate 7 web Topic Ideas on the given topic: {}\n for the related web:  {} \n*".format(topic,web),
 
 
  # temperature=0,
  # max_tokens=54,
  # top_p=1.0,
  # frequency_penalty=0.0,
  # presence_penalty=0.0,
  # stop=["###"])
  # stop=["###"])
  response = openai.Completion.create(
  model="text-davinci-003",
  prompt="convert python django language into c#, java,c++,R language\n\nC#:\n".format(web),
  
  temperature=0.7,
  max_tokens=260,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0)
  
    
  if 'choices' in response:
      if len(response['choices'])>0:
         res = response['choices'] [0]['text']
         
      else:
         return []
  else:
      return []
  a_list = res.split('\n')
  if len (a_list)>0:
    for blog in a_list:
        web_topics.append(blog)
  else:
    return []
  return web_topics




def generateWebSectionTitles(topic,web):
        web_sections = []
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt="##### Translate this function  from Python into Haskell\n### Python\n    \n    def predict_proba(X: Iterable[str]):\n        return np.array([predict_one_probas(tweet) for tweet in X])\n    \n### Haskell".format(topic,web),
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)
#         response = openai.Completion.create(
#         model="code-davinci-002",
#         # prompt="##### Translate this function  from Python into Haskell\n### Python\n    \n    def predict_proba(X: Iterable[str]):\n        return np.array([predict_one_probas(tweet) for tweet in X])\n    \n### Haskell".format(topic,web),
#         prompt="Generate 10 Blog Topic Ideas on the given topic: {}\n for the related web:  {} \n*".format(topic,web),
        
#         temperature=0,
#         max_tokens=54,
#         top_p=1.0,
#         frequency_penalty=0.0,
#         presence_penalty=0.0,
#         stop=["###"]
# )
    
        if 'choices' in response:
            if len(response['choices'])>0:
              res = response['choices'] [0]['text']
            else:
              return []
        else:
            return []
        a_list = res.split('*') 
        if len (a_list)>0:
          for web in a_list:
              web_sections.append(web)
        else:
          return []
        return web_sections





def generateWebSectionDetails(webTopic,sectionTopic,web,prevWeb,profile):
        
      # response = openai.Completion.create(
      # model="code-davinci-002",
      # # prompt="##### Translate this function  from Python into Haskell\n### Python\n    \n    def predict_proba(X: Iterable[str]):\n        return np.array([predict_one_probas(tweet) for tweet in X])\n    \n### Haskell".format(webTopic,sectionTopic,web,prevWeb,profile),
      #   prompt="Generate detailed blog section write up for the following blog section heading,using the web title,web  provided\n\nWeb Title: {}\n\nWeb Section Heading : {}\nWeb : {}\prevBlog :{}\n\n\n".format(webTopic,sectionTopic,web,prevWeb,profile),
     
      
      # temperature=0,
      # max_tokens=54,
      # top_p=1.0,
      # frequency_penalty=0.0,
      # presence_penalty=0.0,
      # stop=["###"])
      response = openai.Completion.create(
        model="text-davinci-003",
        prompt="##### Translate this function  from Python into Haskell\n### Python\n    \n    def predict_proba(X: Iterable[str]):\n        return np.array([predict_one_probas(tweet) for tweet in X])\n    \n### Haskell".format(webTopic,sectionTopic,web,prevWeb,profile),
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)
    
      if 'choices' in response:
        if len(response['choices'])>0:
          res = response['choices'] [0]['text']
          if not res == '':
            cleanedRes =res.replace('\n','<br>')
            if profile.monthlyCount:
              oldCount = int(profile.monthlyCount)
            else:
              oldCount = 0
              oldCount += len(cleanedRes.split(' '))
              profile.monthlyCount = str(oldCount)
              profile.save()
            return cleanedRes
          else:
            return ''  
          
        else:
            return ''
      else:
          return ''










#######################################################

def generateBlogTopicIdeas(topic,audience,keywords):
  blog_topics = []
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Generate 7 Blog Topic Ideas on the given topic: {}\n for the related audience: {}\n keywords: {} \n*".format(topic,audience,keywords),
    temperature=0.7,
    max_tokens=250,
    top_p=1,
    best_of=2,
    frequency_penalty=0,
    presence_penalty=0)
    
  if 'choices' in response:
      if len(response['choices'])>0:
         res = response['choices'] [0]['text']
      else:
         return []
  else:
      return []
  a_list = res.split('*') 
  if len (a_list)>0:
    for blog in a_list:
        blog_topics.append(blog)
  else:
    return []
  return blog_topics

  
def generateBlogSectionTitles(topic,audience,keywords):
        blog_sections = []
        response = openai.Completion.create(
          model="text-davinci-003",
          prompt="Generate 10 Blog Topic Ideas on the given topic: {}\n for the related audience: {}\n keywords: {} \n*".format(topic,audience,keywords),
          temperature=0.7,
          max_tokens=250,
          top_p=1,
          best_of=2,
          frequency_penalty=0,
          presence_penalty=0)
    
        if 'choices' in response:
            if len(response['choices'])>0:
              res = response['choices'] [0]['text']
            else:
              return []
        else:
            return []
        a_list = res.split('*') 
        if len (a_list)>0:
          for blog in a_list:
              blog_sections.append(blog)
        else:
          return []
        return blog_sections
      
      
def generateBlogSectionDetails(blogTopic,sectionTopic,audience,keywords,prevBlog,profile):
        
      response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Generate detailed blog section write up for the following blog section heading,using the blog title,audience and keywords provided\n\nBlog Title: {}\n\nBlog Section Heading : {}\nAudience : {}\nKeywords : {}\prevBlog :{}\n\n\n".format(blogTopic,sectionTopic,audience,keywords,prevBlog),
        # prompt="Generate 10 Blog Topic Ideas on the given topic. {}\nBlog Title:  {}\nBlog Section Headings: {}\naudience: {}\nkeywords: {} \n\n".format(blogTopic,sectionTopic,audience,keywords),
        temperature=0.7,
        max_tokens=2000,
        top_p=1,
        best_of=1,
        frequency_penalty=0,
        presence_penalty=0)
    
      if 'choices' in response:
        if len(response['choices'])>0:
          res = response['choices'] [0]['text']
          if not res == '':
            cleanedRes =res.replace('\n','<br>')
            if profile.monthlyCount:
              oldCount = int(profile.monthlyCount)
            else:
              oldCount = 0
            oldCount += len(cleanedRes.split(' '))
            profile.monthlyCount = str(oldCount)
            profile.save()
            return cleanedRes
          else:
            return ''  
          
        else:
            return ''
      else:
          return ''
          
   
 
def checkCountAllowance(profile):
      if profile.subscribed:
          type = profile.subscriptionType
          if type == 'free':
            max_limit = 5000
            if profile.monthlyCount:
                if int(profile.monthlyCount) < max_limit:
                  return True
                else:
                  return False
            else:
                return True
                
          
          elif type == 'starter':
            max_limit = 40000
            if profile.monthlyCount:
                if int(profile.monthlyCount) < max_limit:
                  return True
                else:
                  return False
            else:
                return True
          
          
          elif type == 'advanced':
              return True
          else:
              return False
      else:
          max_limit = 5000
          if profile.monthlyCount:
              if int(profile.monthlyCount) < max_limit:
                return True
              else:
                return False
          else:
              return True
              
       
def getNextSubscriptionDate(profile):
  subId = profile.subscriptionReference
  if subId:
    try:
      
      url = '{{base_url}}/v1/billing/subscriptions/{}'.format(subId)
      headers = {}
      headers['Authorization'] = settings.PAYPAL_SECRET
      r= requests.get(url,headers = headers)
      response = json.loads(r.text)

    
      if 'status' in response :
        # print (r.text)
        status = response ['status']
        if status == 'Active':
          next_date = response ['billing_info']['next_billing_time'].split('T')[0]
          return next_date
        else:
                profile.subscribed= False
                profile.subscriptionType= 'free'
                profile.save()
                # return 'none'
                today = datetime.datetime.now().day
                day_created = profile.date.created.day
            
                if day_created >today:
                  next_date = datetime.datetime.now()
                  next_month = returnMonth(next_date.month)
                  year = next_date.year
                else:
                  next_date = datetime.datetime.now() + relativedelta(months = 1)
                  next_month = returnMonth(next_date.month)
                  year = next_date.year
              
                return ' {} {} {} '. format (day_created,next_month,year)
          
    except:
        profile.subscribed = False  
        profile.subscriptionType = 'free'
        profile.save()  
        today = datetime.datetime.now().day
        day_created = profile.date.created.day
            
        if day_created >today:
              next_date = datetime.datetime.now()
              next_month = returnMonth(next_date.month)
              year = next_date.year
        else:
              next_date = datetime.datetime.now() + relativedelta(months = 1)
              next_month = returnMonth(next_date.month)
              year = next_date.year
              
        return ' {} {} {} '. format (day_created,next_month,year)
      
             
               
              

 
   

 
# def generateBlogSectionHeadings(topic,audience,keywords):
#     response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="Generate Blog Section Headings and section titles, based on the following blog section topic.\nTopic: {} \nKeywords: {}\n*".format(topic,keywords),
#   temperature=0.7,
#   max_tokens=250,
#   top_p=1,
#   best_of=2,
#   frequency_penalty=0,
#   presence_penalty=0
# )
    
#     if 'choices' in response:
#       if len(response['choices'])>0:
#          res = response['choices'] [0]['text']
#       else:
#          res = None
#     else:
#       res = None
#     return res
  

# res = generateBlogTopicIdeas(topic,keywords).replace('\n', '')
# b_list = res.split('*')
# for blog in b_list:
#   blog_topics.append(blog)
#   print('\n')
#   print(blog)
  
  




