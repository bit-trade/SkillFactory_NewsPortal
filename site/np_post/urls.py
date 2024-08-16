from django.urls import path
from .views import SectionsList, SectionDetail, SectionCreate, SectionUpdate, SectionDelete


urlpatterns = [
    path('', SectionsList.as_view(), name='sections'),
    path('<int:pk>/', SectionDetail.as_view(), name='section_detail'),
    path('create/', SectionCreate.as_view(), name='section_create'),
    path('<int:pk>/edit/', SectionUpdate.as_view(), name='section_edit'),
    path('<int:pk>/delete/', SectionDelete.as_view(), name='section_delete'),
]