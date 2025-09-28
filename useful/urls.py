from django.urls import path

from useful.views import ArticleView, DocumentView, ShowUseful, ShowUsefulRegulatoryDocs, ShowUsefulArticlesAndLinks

app_name = 'useful'

urlpatterns = [
    path('', ShowUseful.as_view(), name='useful'),
    path('regulatory_docs/', ShowUsefulRegulatoryDocs.as_view(), name='useful_regulatory_docs'),
    path('regulatory_docs/<slug:slug>/', DocumentView.as_view(), name='useful_document'),
    path('articles_and_links/', ShowUsefulArticlesAndLinks.as_view(), name='useful_articles_and_links'),
    path('articles_and_links/<slug:slug>/', ArticleView.as_view(), name='useful_article'),

]