from django.urls import path
from .views import ArticlesList, PublicDetail, ArticleCreate, PublicUpdate, PublicDelete
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', cache_page(300)(ArticlesList.as_view()), name='articles'),
    path('<int:pk>', PublicDetail.as_view(), name='public_detail'),
    path('create/', ArticleCreate.as_view(), name='article_create'),
    path('<int:pk>/edit/', PublicUpdate.as_view(), name='public_edit'),
    path('<int:pk>/delete/', PublicDelete.as_view(), name='public_delete'),
]
