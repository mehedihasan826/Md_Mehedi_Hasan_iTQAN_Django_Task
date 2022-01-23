from django.urls import path
from .views import CategoryListView, CategoryDetailsView, ProductDetailsView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('product/<int:pk>', login_required(ProductDetailsView.as_view()), name='product_details'),
    path('category/<int:pk>', login_required(CategoryDetailsView), name='category_details'),
    path('', login_required(CategoryListView.as_view()), name='home'),
    # path('')
]