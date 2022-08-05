from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


from django.views import generic 
from django.contrib.auth.forms import UserCreationForm




def index(request):
	return render(request, 'hi/index.html')

def CategoryListView(request):
	category_menu_list = Category.objects.all()
	return render(request,'categories_list.html',{'category_menu_list': category_menu_list})

def CategoryView(request, category):
	category_posts = Post.objects.filter(category=category.replace('-',' '))
	return render(request,'categories.html',{'category': category.title().replace('-',' '),'category_posts':category_posts})

class HomeView(ListView):
	model = Post
	template_name = 'hi/index.html'
	ordering = ['-post_date']
	#ordering = ['-id']

	def get_context_data(self, *args, **kwargs):
		category_menu = Category.objects.all()
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		context["category_menu"] = category_menu
		return context




class ArticleView(DetailView):
	model = Post
	template_name = 'hi/article_detail.html'
	def get_context_data(self, *args, **kwargs):
		category_menu = Category.objects.all()
		context = super(ArticleView, self).get_context_data(*args, **kwargs)
		context["category_menu"] = category_menu
		return context

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'
	#fields = '__all__'
	#fields = ('title','body')

class AddCategoryView(CreateView):
	model = Category
	template_name = 'add_category.html'
	fields = '__all__'
	#fields = ('title','body')


class UpdatePostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'hi/update_post.html'
	#fields = ['title','title_tag','body']
class DeletePostView(DeleteView):
	model = Post
	template_name = 'hi/delete_post.html'
	success_url = reverse_lazy('Home')


