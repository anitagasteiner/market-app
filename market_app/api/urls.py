from django.urls import include, path
from .views import MarketsView, MarketDetail, SellerOfMarketList, SellersView, SellerDetail, ProductViewSet, ProductsView, ProductDetail
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('market/', MarketsView.as_view()),
    path('market/<int:pk>/', MarketDetail.as_view(), name='market-detail'),
    path('market/<int:pk>/sellers/', SellerOfMarketList.as_view()),
    path('seller/', SellersView.as_view()),
    path('seller/<int:pk>/', SellerDetail.as_view(), name='seller-detail'),
    #path('product/', ProductsView.as_view()),
    #path('product/<int:pk>/', ProductDetail.as_view(), name='product-detail')
]

