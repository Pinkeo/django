from django.contrib import admin
from django.urls import path,  include
#from hi.views import index
from hi.views import HomeView, ArticleView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView
from members.views import UserRegisterView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),

    path('', HomeView.as_view(), name = "Home"),
    path('article/<int:pk>', ArticleView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),

    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:category>/', CategoryView, name = 'category'),
    path('category-list/', CategoryListView, name = 'category-list'),


    path('register/', UserRegisterView.as_view(), name = 'register'),
   
]

