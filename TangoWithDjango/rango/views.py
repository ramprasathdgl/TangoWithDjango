from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from rango.models import Category

def index(request):
	#context         = RequestContext(request)
	category_list   = Category.objects.order_by('likes')[:5]
	context_dict    = {'categories':category_list}
	#return render_to_response('rango/index.html', context_dict, context)
	return render(request,'rango/index.html',context_dict)
    #return HttpResponse("Rango says: Hello world! <a href='/rango/about'>About</a>")

def about(request):
	#context         = RequestContext(request)
	context_dict    = {'boldmessage':"I am bold font"}
	#return render_to_response('rango/about.html', context_dict, context)
	#return HttpResponse("<a href='/rango/'>Index</a>")
	return render(request,'rango/about.html',context_dict)



