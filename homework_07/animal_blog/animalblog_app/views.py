from django.views.generic import TemplateView

from animalblog_app.models import Article, Author


class ArticlesIndexView(TemplateView):
    template_name = 'animalblog_app/articles_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            # products=Product.objects.all(),
            articles=(
                Article.objects
                .select_related("author")
                .all()
                ),
            )
        return context

class AuthorsIndexView(TemplateView):
    template_name = "animalblog_app/authors_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(

            authors=(
                Author.objects.all()
            ),
        )
        return context