from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
	context         = RequestContext(request)
	context_dict    = {'boldmessage':"I am bold font"}
	return render_to_response('rango/index.html', context_dict, context)
    #return HttpResponse("Rango says: Hello world! <a href='/rango/about'>About</a>")

def about(request):
	context         = RequestContext(request)
	context_dict    = {'boldmessage':"I am bold font"}
	return render_to_response('rango/about.html', context_dict, context)
	#return HttpResponse("<a href='/rango/'>Index</a>")



