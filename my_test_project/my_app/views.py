from django.shortcuts import render

from django.http import HttpResponse

#its request for my_app like ma koree keverrr
def _defalt(request):
    return HttpResponse("<h1>welcome to my first website :)</h1>")


def index(request):
    return HttpResponse("<h1> the lion king is bar harush </h1>")

def liron(request):
    return HttpResponse("<h1> I LOVE liron (tree) </h1>")

def daniela(request):
    return HttpResponse("<h1> love you <3 dandon  , happy birthday")
def matan(request):
    return HttpResponse("<h1> More then words")

def daniel(request):
    return HttpResponse("<h1> Daniel, sorry again that I'm late because I'm on the computer <3.")

def oriya(request):
    
    return HttpResponse("<h1>Ze Ani , shesrpti et atost emsh</h1>")
#its write with html title 
#def index(request):
     #html = "<p> Hello </p> <br> <p>world</p>"
     #return HttpResponse(html)




#def index(request): 
    #res = HttpResponse()
    #res.write("<h1> some text inside html tag </h1>")
    #res.write("<h1> some other text inside html tag </h1>")
    #return res