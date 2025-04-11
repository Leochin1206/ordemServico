from django.http import HttpResponse
from .models import Ambientes, Gestores, Manutentores, OrdemServico, Responsaveis, Patrimonios
from .serializer import AmbientesSerializer, GestoresSerializer, ManutentoresSerializer, OrdemServicoSerializer, ResponsaveisSerializer, PatrimoniosSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_role_decorator

# ======================= Ambientes =======================

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def listar_ambientes(request):
    if request.method == 'GET':
        queryset = Ambientes.objects.all()
        serializer = AmbientesSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AmbientesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class AmbientesView(ListCreateAPIView):
    queryset = Ambientes.objects.all()
    serializer_class = AmbientesSerializer
    permission_classes = [IsAuthenticated]

class AmbientesDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Ambientes.objects.all()
    serializer_class = AmbientesSerializer
    permission_classes = [IsAuthenticated]

class AmbientesSearchView(ListAPIView):
    queryset = Ambientes.objects.all()
    serializer_class = AmbientesSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ['num_sala', 'num_sig', 'descricao_sig', 'ni', 'responsavel']

# ======================= Gestores =======================

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def listar_gestores(request):
    if request.method == 'GET':
        queryset = Gestores.objects.all()
        serializer = GestoresSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = GestoresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class GestoresView(ListCreateAPIView):
    queryset = Gestores.objects.all()
    serializer_class = GestoresSerializer
    permission_classes = [IsAuthenticated]

class GestoresDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Gestores.objects.all()
    serializer_class = GestoresSerializer
    permission_classes = [IsAuthenticated]

class GestoresSearchView(ListAPIView):
    queryset = Gestores.objects.all()
    serializer_class = GestoresSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ['nome', 'ni', 'cargo', 'area']

# ======================= Manutentores =======================

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def listar_manutentores(request):
    if request.method == 'GET':
        queryset = Manutentores.objects.all()
        serializer = ManutentoresSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ManutentoresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ManutentoresView(ListCreateAPIView):
    queryset = Manutentores.objects.all()
    serializer_class = ManutentoresSerializer
    permission_classes = [IsAuthenticated]

class ManutentoresDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Manutentores.objects.all()
    serializer_class = ManutentoresSerializer
    permission_classes = [IsAuthenticated]

class ManutentoresSearchView(ListAPIView):
    queryset = Manutentores.objects.all()
    serializer_class = ManutentoresSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ['nome', 'email', 'ni', 'area']

# ======================= OrdemServico =======================

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def listar_OrdemServico(request):
    if request.method == 'GET':
        queryset = OrdemServico.objects.all()
        serializer = OrdemServicoSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OrdemServicoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class OrdemServicoView(ListCreateAPIView):
    queryset = OrdemServico.objects.all()
    serializer_class = OrdemServicoSerializer
    permission_classes = [IsAuthenticated]

class OrdemServicoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = OrdemServico.objects.all()
    serializer_class = OrdemServicoSerializer
    permission_classes = [IsAuthenticated]

class OrdemServicoSearchView(ListAPIView):
    queryset = OrdemServico.objects.all()
    serializer_class = OrdemServicoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ['descricao_servico', 'data_abertura', 'data_encerramento', 'status', 'prioridade', 'patrimonio', 'ambiente', 'responsavel', 'manutentor']

# ======================= Responsaveis =======================

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def listar_responsaveis(request):
    if request.method == 'GET':
        queryset = Responsaveis.objects.all()
        serializer = ResponsaveisSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ResponsaveisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ResponsaveisView(ListCreateAPIView):
    queryset = Responsaveis.objects.all()
    serializer_class = ResponsaveisSerializer
    permission_classes = [IsAuthenticated]

class ResponsaveisDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Responsaveis.objects.all()
    serializer_class = ResponsaveisSerializer
    permission_classes = [IsAuthenticated]

class ResponsaveisSearchView(ListAPIView):
    queryset = Responsaveis.objects.all()
    serializer_class = ResponsaveisSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ['nome', 'email', 'ni', 'gestor']

# ======================= Patrimonios =======================

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def listar_patrimonios(request):
    if request.method == 'GET':
        queryset = Patrimonios.objects.all()
        serializer = PatrimoniosSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PatrimoniosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class PatrimoniosView(ListCreateAPIView):
    queryset = Patrimonios.objects.all()
    serializer_class = PatrimoniosSerializer
    permission_classes = [IsAuthenticated]

class PatrimoniosDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Patrimonios.objects.all()
    serializer_class = PatrimoniosSerializer
    permission_classes = [IsAuthenticated]

class PatrimoniosSearchView(ListAPIView):
    queryset = Patrimonios.objects.all()
    serializer_class = PatrimoniosSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ['localizacao', 'ni', 'descricao']

# ============================= SignUp =============================

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if username is None or password is None:
        return Response({'error': 'Username and password required'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password)
    return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

def register_gestor(request):
    user = User.objects.create_user(username='elleo', password='123')
    user.save()
    assign_role(user, 'gestores')
    return HttpResponse('usuario salvo')