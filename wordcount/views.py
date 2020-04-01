from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    wlist = fulltext.split()

    worddic = {}

    for word in wlist:
        if word in worddic:
            worddic[word] += 1
        else:
            worddic[word] = 1

    sortedwards = sorted(worddic.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',{'fulltext':fulltext,'count':len(wlist),'sortedwards':sortedwards})

def about(request):
    return render(request, 'about.html')
