from django.urls import path
from .views import MarketsView, market_single_view, SellersView, seller_single_view, ProductsView, product_single_view

urlpatterns = [
    path('market/', MarketsView.as_view()),
    path('market/<int:pk>/', market_single_view, name='market-detail'),
    path('seller/', SellersView.as_view()),
    path('seller/<int:pk>/', seller_single_view, name='seller_single'),
    path('product/', ProductsView.as_view()),
    path('product/<int:pk>/', product_single_view, name='product_single')
]

