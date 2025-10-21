from rest_framework import serializers
from market_app.models import Market, Seller, Product


def validate_no_x(value): # wird normalerweise in extra Datei geschrieben
    errors = []
    if 'X' in value:
        errors.append('No X in location!')
    if 'Y' in value:
        errors.append('No Y in location!')
    if errors:
        raise serializers.ValidationError(errors)
    return value


class MarketSerializer(serializers.ModelSerializer):
    sellers = serializers.StringRelatedField(many=True, read_only=True)    
    class Meta:
        model = Market
        #fields = '__all__'
        fields = ['name', 'description', 'location', 'net_worth', 'sellers']
        #exclude = []

    def validate_name(self, value):
        errors = []
        if 'X' in value:
            errors.append('No X in name!')
        if 'Y' in value:
            errors.append('No Y in name!')
        if errors:
            raise serializers.ValidationError(errors)
        return value
        

class MarketHyperlinkedSerializer(MarketSerializer, serializers.HyperlinkedModelSerializer):

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None) # Von den Parametern, die ich später übergebe, poppe ich das "fields" raus, wenn das möglich ist.

        # Die Standard-init-Funktion wird aufgerufen:
        super().__init__(*args, **kwargs)

        if fields is not None: # Wenn ich etwas übergebe, wenn "fields" nicht None ist, dann schaue ich, ob es drin ist.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name) # Ich poppe alles raus, was nicht drin ist.
            
    class Meta:
        model = Market
        # Dafür muss ich die Fields definieren:
        fields = ['id', 'name', 'location', 'description', 'net_worth', 'sellers', 'url']


class SellerSerializer(serializers.ModelSerializer):
    markets = MarketSerializer(many=True, read_only=True)
    #markets = serializers.StringRelatedField(many=True)
    market_ids = serializers.PrimaryKeyRelatedField(
        queryset=Market.objects.all(),
        many=True,
        write_only=True,
        source='markets'
    )
    market_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Seller
        exclude = []
        #fields = ['id', 'name', 'market_ids', 'market_count', 'markets', 'contact_info']

    def get_market_count(self, obj):
        return obj.markets.count()


class SellerHyperlinkedSerializer(SellerSerializer, serializers.HyperlinkedModelSerializer):
    markets = serializers.StringRelatedField(many=True)    

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)

        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
            
    class Meta:
        model = Seller
        fields = ['id', 'name', 'contact_info', 'market_count', 'markets', 'url']


class ProductSerializer(serializers.ModelSerializer):
    #markets = serializers.StringRelatedField(many=True)
    markets = MarketSerializer(read_only=True)
    market_ids = serializers.PrimaryKeyRelatedField(
        queryset=Market.objects.all(),
        write_only=True,
        source='markets'
    )
    #sellers = serializers.StringRelatedField(many=True)
    sellers = SellerSerializer(read_only=True)
    seller_ids = serializers.PrimaryKeyRelatedField(
        queryset=Seller.objects.all(),
        write_only=True,
        source='sellers'
    )

    class Meta:
        model = Product
        fields = '__all__'


