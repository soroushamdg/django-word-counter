from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def count(request):
    text = request.GET['fulltext']
    wordlist = text.split()
    worddict = {}
    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1
    return render(request, 'count.html',{'fulltext':len(wordlist),'words':worddict.items()})
def about(request):
    return render(request, 'about.html')