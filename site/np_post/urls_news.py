from django.urls import path
from .views import NewsList, PublicDetail, NewsCreate, PublicUpdate, PublicDelete


urlpatterns = [
    path('', NewsList.as_view(), name='news'),
    path('<int:pk>', PublicDetail.as_view(), name='public_detail'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/edit/', PublicUpdate.as_view(), name='public_edit'),
    path('<int:pk>/delete/', PublicDelete.as_view(), name='public_delete'),
]
