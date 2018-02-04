from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Article
from .forms import CreateArticleForm

# Create your views here.
def all(request):
    args = {
        'articles': Article.objects.all()
    }
    return render(request, 'test-all.html', args)

def get(request, article_id=0):
    try:
        args = {
            'article': Article.objects.get(id=article_id)
        }
        return render(request, 'test-get.html', args)
    except Article.DoesNotExist:
        return render(request, 'test-404.html')

@login_required(login_url='/users/login/?next=/articles/create/')
def create(request):
    user = request.user
    article = Article(user=user)
    if request.method == 'POST':
        req = {
            'user': user,
            'title': request.POST.get('title', ''),
            'body': request.POST.get('body', ''),
        }
        form = CreateArticleForm(data=req, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('/articles/all/')
    else:
        form = CreateArticleForm(instance=article)
    return render(request, 'test-create.html', {'form': form})
