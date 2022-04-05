from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from videos import views
app_name = "article"

urlpatterns = [
    path('dashboard/', views.dashboard, name = "dashboard"),
    path('addarticle/', views.addArticle, name = "add article"),
    path('article/<int:id>/', views.detail, name = "detail"),
    path('update/<int:id>', views.updateArticle, name="update"),
    path('delete/<int:id>', views.deleteArticle, name="delete"),
    path('', views.articles, name="articles"),
    path('comment/<int:id>', views.addComment, name="comment")
]
if settings.DEBUG:  # Dev only
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
