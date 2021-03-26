#New file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse('Hello')
    return render(request,'index.html')

def analyze(request):
    #get the text
    djtext=request.GET.get('text','default')

    #check checkbox value
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcount = request.GET.get('charcount', 'off')
    check=0

    if removepunc == "on":
        check = 1
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=''
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        params={'purpose':'After Removing Punctuations','analyzed_text':analyzed}
        djtext=analyzed

    if fullcaps == 'on':
        check = 1
        analyzed=""
        for char in djtext:
            analyzed+=char.upper()
        params = {'purpose': 'Change to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if (extraspaceremover == "on"):
        check = 1
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        djtext=analyzed

    if (newlineremover == "on"):
        check = 1
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != '\r':
                analyzed += char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        djtext = analyzed

    if charcount =='on':
        check = 1
        params = {'purpose': 'Total characters', 'analyzed_text': len(''.join(djtext.split()))}
        djtext=analyzed


    if check==1 :
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("error")
