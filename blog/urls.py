from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.indexPage, name = 'indexPage'),
    path('add_blog/', views.add_blog, name = 'add_blog'),
    path('edit_blog/<int:blog_id>/', views.edit_blog, name = 'edit_blog'),
    path('delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path('view_blog/<int:blog_id>/', views.view_blog, name = 'view_blog'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 