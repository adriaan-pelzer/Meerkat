from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

def homepage(request):
    return render_to_response(
        'homepage.html', {}, RequestContext(request))

def submit(request):
    return render_to_response(
        'submit.html', {}, RequestContext(request))

def actor(request, actor_id=None):
    return render_to_response(
        'actor_index.html', {}, RequestContext(request))

def meerkatter(request, meerkatter_id=None):
    return render_to_response(
        'meerkatter_index.html', {}, RequestContext(request))

def register(request):
    return render_to_response(
        'register.html', {}, RequestContext(request))
