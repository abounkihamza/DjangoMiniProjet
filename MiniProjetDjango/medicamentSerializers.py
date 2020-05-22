from rest_framework import serializers
from MiniProjetDjango.models import *

class medicamentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Medicament
        fields="__all__"