from django.shortcuts import render
from .forms import Tweet
from .models import Comment
# Create your views here.

def index(request):
        form = Tweet(request.POST or None)
        if form.is_valid():
            author = form.cleaned_data.get("author")
            comment = form.cleaned_data.get("content")
            print(author)
            print(comment)
            tweet = Comment(author=author, comment=comment)
            tweet.save()
        context = {'form': form}
        return render(request, "index.html", context)

def comment_view(request):
    # form = Tweet(request.POST or None)
    # # print(form)
    # if form.is_valid():
    #     author = form.cleaned_data.get("author")
    #     comment = form.cleaned_data.get("content")
    #     print(author)
    #     tweet = Comment(author=author, comment=comment)
    #     tweet.save()
    # context = {'form': form}
    return render(request, "comments/comment.html")

def form_view(request):
    form = Tweet(request.POST or None)
    print(form)
    if form.is_valid():
        author = form.cleaned_data.get("author")
        comment = form.cleaned_data.get("content")
        print(author)
        tweet = Comment(author=author, comment=comment)
        tweet.save()
    context = {'form': form}

    return render(request, "comments/form.html", context)