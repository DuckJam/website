from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name = "about"),
    path("post/<pk>/", views.post, name = "post"),
    path("project/<slug:project_title_slug>/", views.project, name = "project")
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)