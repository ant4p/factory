from django.urls import reverse
from django.views.generic import DetailView, ListView, TemplateView

from useful.models import Article, Document


# class ShowUseful(TemplateView):
#     template_name = "useful/useful.html"


class ShowUsefulRegulatoryDocs(ListView):
    template_name = "useful/regulatory_docs.html"
    context_object_name = "items"
    paginate_by = 5

    def get_queryset(self):
        return Document.objects.all()


class ShowUsefulArticlesAndLinks(ListView):
    template_name = "useful/articles_and_links.html"
    context_object_name = "items"
    paginate_by = 5

    def get_queryset(self):
        return Article.objects.all()


class ArticleView(DetailView):
    model = Article
    template_name = "useful/article.html"
    context_object_name = "item"

    def get_queryset(self):
        return Article.objects.filter()

    def get_success_url(self):
        return reverse("article", kwargs={"slug": self.object.slug})


class DocumentView(DetailView):
    model = Document
    template_name = "useful/document.html"
    context_object_name = "item"

    def get_queryset(self):
        return Document.objects.filter()

    def get_success_url(self):
        return reverse("document", kwargs={"slug": self.object.slug})
