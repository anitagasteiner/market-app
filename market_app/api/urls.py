from django.urls import path
from .views import MarketsView, MarketDetail, SellerOfMarketList, SellersView, SellerDetail, ProductsView, product_single_view

urlpatterns = [
    path('market/', MarketsView.as_view()),
    path('market/<int:pk>/', MarketDetail.as_view(), name='market-detail'),
    path('market/<int:pk>/sellers/', SellerOfMarketList.as_view()),
    path('seller/', SellersView.as_view()),
    path('seller/<int:pk>/', SellerDetail.as_view(), name='seller_single'),
    path('product/', ProductsView.as_view()),
    path('product/<int:pk>/', product_single_view, name='product_single')
]

