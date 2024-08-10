from django.urls import path
from .views import Subscription, SubsCreate, SubsUpdate


urlpatterns = [
    path('<int:pk>/', Subscription.as_view(), name='subs_detail'),
    path('create/', SubsCreate.as_view(), name='subs_create'),
    path('<int:pk>/edit/', SubsUpdate.as_view(), name='subs_edit'),
]
