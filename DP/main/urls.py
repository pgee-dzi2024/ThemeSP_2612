# main/urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # Път към основната страница (Frontend-а)
    path('', views.index, name='index'),

    # Път към нашето API за приемане на команди
    path('api/command/', views.send_command, name='send_command'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)