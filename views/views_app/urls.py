from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.AuthorList.as_view(), name='author_list'),
    path('authors/create/', views.CreateAutorView.as_view(), name='author_create'),
    path('authors/<int:pk>/', views.AuthorDetail.as_view(), name='author_detail'),
    path('authors/<int:pk>/update/', views.UpdateAuthorView.as_view(), name='author_update'),
    path('authors/<int:pk>/delete/', views.DeleteAuthorView.as_view(), name='author_delete'),

    path('posts/', views.PostList.as_view(), name='post_list'),
    path('posts/create/', views.CreatePostView.as_view(), name='post_create'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('posts/<int:pk>/update/', views.UpdatePostView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.DeletePostView.as_view(), name='post_delete'),

    path('categories/', views.CategoryList.as_view(), name='category_list'),
    path('categories/create/', views.CreateCategoryView.as_view(), name='category_create'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='category_detail'),
    path('categories/<int:pk>/update/', views.UpdateCategoryView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete', views.DeleteCategoryView.as_view(), name='category_delete'),

    path('', views.MainPage.as_view(), name='main_page'),
    path('paginator_authors/', views.paginator_view),
    path('user_registration/', views.UserRegistrationView.as_view()),
    path('create_category/', views.add_record),
    path('<int:pk>/', views.update_category),
    path('author_search/', views.author_search),
    path('authors_formset/', views.authors),
    path('captcha/', views.CaptchaView.as_view())
]
