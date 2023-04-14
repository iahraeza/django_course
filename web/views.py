from django.shortcuts import render,redirect
from . models import Post
from . forms import addpostForm
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
def post_view(request):
    posts=Post.objects.all()
    return render(request,"web/post_view.html",{"posts":posts})
def post_detail(request, pk):
    posst=get_object_or_404(Post, pk=pk)
    return render(request, 'web/detail_view.html', {'posst': posst})
def post_show_publish(request):
    post_list=Post.objects.filter(status='PUB')
    return render(request, "web/post_list.html", {"post_list": post_list})


def postadd(request):
    if request.method == 'POST':
        # create an instance of the addpostForm form class using POST data
        form = addpostForm(request.POST)
        if form.is_valid():
            # save form data to the database
            post = form.save()
            # create a new instance of the addpostForm form class
            form = addpostForm()
    else:
        # create an instance of the addpostForm form class
        form = addpostForm()

    # render the addpost.html template with the form object passed in as context data
    return render(request, "web/addpost.html", {"form": form})


def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form =addpostForm(request.POST or None,instance=post)
        if form.is_valid():
            form.save()
            return render(request,'web/addpost.html',{"form":form})
    else:
        form =addpostForm(instance=post)

    return render(request, "web/update.html", {"form": form})

def delete_post(request,pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            post.delete()
            return redirect('post_view')
        return render(request, "web/delet.html", {"post": post})



