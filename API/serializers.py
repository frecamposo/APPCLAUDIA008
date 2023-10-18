from .models import Receta
from rest_framework import serializers

class RecetaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = "__all__"
