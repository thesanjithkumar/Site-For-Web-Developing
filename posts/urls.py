from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from posts import views

app_name = 'post'

urlpatterns = [
    path('list/', views.blog_view, name='list'),
    path('<int:id>/', views.detail_view, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
