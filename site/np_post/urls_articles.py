from django.urls import path
from .views import ArticlesList, PublicDetail, ArticleCreate, PublicUpdate, PublicDelete


urlpatterns = [
    path('', ArticlesList.as_view(), name='articles'),
    path('<int:pk>', PublicDetail.as_view(), name='public_detail'),
    path('create/', ArticleCreate.as_view(), name='article_create'),
    path('<int:pk>/edit/', PublicUpdate.as_view(), name='public_edit'),
    path('<int:pk>/delete/', PublicDelete.as_view(), name='public_delete'),
]
