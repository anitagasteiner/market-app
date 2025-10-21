from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MarketSerializer, MarketHyperlinkedSerializer, SellerSerializer, SellerHyperlinkedSerializer, ProductSerializer, ProductHyperlinkedSerializer
from market_app.models import Market, Seller, Product
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics


class MarketsView(generics.ListCreateAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketHyperlinkedSerializer


class MarketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer


class SellerOfMarketList(generics.ListAPIView):
    serializer_class = SellerSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        market = Market.objects.get(pk = pk)
        return market.sellers.all()


class SellersView(generics.ListCreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerHyperlinkedSerializer


class SellerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    

class ProductsView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductHyperlinkedSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
