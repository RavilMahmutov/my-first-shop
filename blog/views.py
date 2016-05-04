from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from .models import Post, Comment, Category, Good
from .forms import PostForm, CommentForm



def post_list(request):
	posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')
	categories = Category.objects.all()
	paginator = Paginator(posts, 5)
	page = request.GET.get('page')
	try:
		posts_page = paginator.page(page)   #Создал переменную posts_page, чтобы не запутаться с основным список постов
	except PageNotAnInteger:
		posts_page = paginator.page(1)  #если номер страницы не число - вернуть первую страницу
	except EmptyPage:
		posts_page = paginator.page(paginator.num_pages)  #если страница вне диапазона, например 9999, то вернет последнюю страницу   

	return render(request, 'blog/post_list.html', {'posts_page':posts_page, 'categories':categories})


def post_detail(request, pk):
	categories = Category.objects.all()
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post, 'categories':categories})

def category(request, pk):
	categories = Category.objects.all()
	category = get_object_or_404(Category, pk=pk)
	return render(request, 'blog/category.html', {'category': category, 'categories':categories})

def good_detail(request, pk):
	categories = Category.objects.all()
	good = get_object_or_404(Good, pk=pk)
	return render(request, 'blog/good_detail.html', {'good': good, 'categories':categories})
