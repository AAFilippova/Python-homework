from django.urls import path

from .views import ArticlesIndexView, AuthorsIndexView

app_name = "animalblog_app"

urlpatterns = [
    path("articles/", ArticlesIndexView.as_view(), name="articles_index"),
    path("authors/", AuthorsIndexView.as_view(), name="authors_index"),
]