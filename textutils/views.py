from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params={'name':"Aaman",'place':'mars'}
    return HttpResponse(render(request,'index.html',params))



def analyze(request):

    # get the text
    djtxt=request. GET.get('text','default')
    removepunc= request.GET.get('removepunc','off')
    fullcaps= request.GET.get('fullcapital','off')
    newLineRemover= request.GET.get('newLineRemover','off')
    extraSpaceRemover= request.GET.get('extraSpaceRemover','off')
    if removepunc=='on':
        # analyzed=djtxt
        Punctuation='''!()_{};:'"[]-<>./,@#$%^&*'''
        analyzed=""
        for char in djtxt:
            if char not in Punctuation:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuation','analyzed_text':analyzed}
        # analyze the text
        return HttpResponse(render(request,'analyze.html',params))
    elif fullcaps=='on':
        analyzed=""
        for char in djtxt:
            analyzed=analyzed+char.upper()
        params={'purpose':'CHANGED TO UPPERCASE','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif newLineRemover=='on':
        analyzed=""
        for char in djtxt:
            if char != "\n":
                analyzed=analyzed+char
        params={'purpose':'REMOVED NEW LINE','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif extraSpaceRemover=='on':
        analyzed=""
        for index ,char in enumerate(djtxt):
            if not (djtxt[index]==" " and djtxt[index+1]==" "):
                analyzed=analyzed+char
        params={'purpose':'REMOVED EXTRA SPACE','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("ERROR 404HAHAHAH")




