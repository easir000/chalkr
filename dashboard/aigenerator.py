from .functions import *



def getDescription(businessName, businessDo):
    length = 265
    description = returnSection1Description(businessName, businessDo)
    if len(description) < length:
        return description
    else:
        desc_list = description.split('. ')
        while True:
            answer = ''
            for desc in desc_list:
                answer += desc
            
            if len(answer)> length:
                desc_list.remove (desc_list(len(desc_list)-1))
                
            else:
                return answer  


def limitToParagraphLength(description, length):
    if len(description)<length:
        return description
    else:
        desc_list= description.split( ' . ')
        if len(desc_list)==1:
            return description
        while True:
            answer = ''
            for desc in desc_list:
                answer += desc
            
            if len(answer)> length:
                desc_list.remove (desc_list(len(desc_list)-1))
                
            else:
                return answer 
            
            