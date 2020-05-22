from rest_framework import serializers
from MiniProjetDjango.models import *

class fournisseurSerializers(serializers.ModelSerializer):
    class Meta:
        model=Fournisseur
        fields="__all__"