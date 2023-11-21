from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name = "about"),
    path("post/<pk>", views.show_post, name = "show_post"),
    path("images/<image_id>", views.show_image, name= "show_image")
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)