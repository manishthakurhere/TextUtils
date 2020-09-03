# I have created this file- Manish
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request, 'index.html')
    return HttpResponse("Home")
def analyze(request):
    djtext=request.POST.get('text', 'default')
    # checking which check boxes are on
    removepunc=request.POST.get('removepunc', 'off')
    fullcaps=request.POST.get('fullcaps', 'off')
    newlineremover=request.POST.get('newlineremover', 'off')
    analyzed=""
    puncs='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    if removepunc == "on":
        for char in djtext:
            if char not in puncs:
                analyzed= analyzed+char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed;

    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to upper case', 'analyzed_text': analyzed}
        djtext=analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed+char
        params= {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext=analyzed

    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on"):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)




