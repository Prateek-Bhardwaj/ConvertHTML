from django.shortcuts import render
from .models import Post
from .forms import PostForm
# Create your views here.

def home(request):
    form = PostForm()
    context = {
        'form':form
    }
    return render(request,'home.html',context)