from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .models import Video, Comments
from .forms import ArticleForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Video.objects.filter(title__contains=keyword)
        return render(request, "articles.html", {"articles": articles})

    articles = Video.objects.all()
    return render(request, "articles.html", {"articles":articles})


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, "about.html")

@login_required(login_url="user:login")
def dashboard(request):
    articles = Video.objects.filter(author=request.user)
    context = {
        "articles": articles
    }
    return render(request, "dashboard.html", context=context)

@login_required(login_url="user:login")
def addArticle(requset):
    form = ArticleForm(requset.POST or None, requset.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = requset.user
        article.save()
        messages.info(requset, 'Article successfully created.')
        return redirect("article:dashboard")

    return render(requset, "addarticle.html", {'form': form})

@login_required(login_url="user:login")
def detail(request, id):
    article = get_object_or_404(Video, id = id)

    comments = article.comments.all()

    return render(request, "detail.html", {"article": article, "comments":comments})


@login_required(login_url="user:login")
def updateArticle(request, id):
    article = get_object_or_404(Video, id = id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.info(request, 'Article successfully updated.')
        return redirect("article:dashboard")

    return render(request, "update.html", {"form":form})
@login_required(login_url="user:login")
def deleteArticle(request, id):
    article = get_object_or_404(Video, id=id)
    article.delete()
    messages.info(request, "Article successfully deleted.")
    return redirect("article:dashboard")


@login_required(login_url="user:login")
def addComment(request, id):
    article = get_object_or_404(Video, id=id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comments(comment_author=comment_author, comment_content=comment_content)

        newComment.article = article

        newComment.save()
        messages.info(request,"Comments successfully added.")
    return redirect(reverse("article:detail", kwargs={"id": id}))
