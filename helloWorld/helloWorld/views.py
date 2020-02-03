from django.views import generic
from django.shortcuts import render

from django.shortcuts import render
def post_list(request):
    return render(request, 'helloWorldTemplate/post_list.html', {})
