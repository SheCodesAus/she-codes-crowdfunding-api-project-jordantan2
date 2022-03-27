from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path("projects/", views.ProjectList.as_view()),
    path("projects/<int:pk>/", views.ProjectDetail.as_view()),
    path("project_product/", views.ProjectProductList.as_view()),
    path("category/", views.CategoryListView.as_view()),
    path("product/", views.ProductListView.as_view()),
    path("product/<int:pk>/", views.ProductDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
