from rest_framework import serializers
from .models import Responsaveis, Patrimonios, Ambientes, Manutentores, OrdemServico, Gestores

class ResponsaveisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsaveis
        fields = '__all__'

class PatrimoniosSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Patrimonios
        fields = '__all__'

class AmbientesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Ambientes
        fields = '__all__'

class ManutentoresSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Manutentores
        fields = '__all__'

class OrdemServicoSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = OrdemServico
        fields = '__all__'

class GestoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gestores
        fields = '__all__'