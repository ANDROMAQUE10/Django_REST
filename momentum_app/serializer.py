from rest_framework.serializers import ModelSerializer
from .models import DJ30, Etf, Divs, Notes, SP500


class SP500Serializer(ModelSerializer):
    class Meta:
        model = SP500
        fields = ["symbol", "name", "avg_momentum", "momentum_12_2", "ep", "low_range"]


class DJ30Serializer(ModelSerializer):
    class Meta:
        model = DJ30
        fields = ["symbol", "name", "avg_momentum", "momentum_12_2", "ep", "low_range"]


class EtfSerializer(ModelSerializer):
    class Meta:
        model = Etf
        fields = ["symbol", "name", "momentum_12_1", "ma10"]


class DivsSerializer(ModelSerializer):
    class Meta:
        model = Divs
        fields = ["symbol", "name", "div_p"]


class NotesSerializer(ModelSerializer):
    class Meta:
        model = Notes
        fields = ["id", "text", "user"]
