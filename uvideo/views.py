from django.http import HttpResponse
from django.shortcuts import render_to_response

def about_us(request):
    return render_to_response('about-us.html', )