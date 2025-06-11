from rest_framework import generics
from .models import (
    Usuario, CientificoDeDatos, Agricultor,
    Cultivo, DatoClimatico, ModeloPredictivo,
    Alerta, Recomendacion
)
from usuario.serializers import (
    UsuarioSerializer, CientificoDeDatosSerializer, AgricultorSerializer,
    CultivoSerializer, DatoClimaticoSerializer, ModeloPredictivoSerializer,
    AlertaSerializer, RecomendacionSerializer
)

# Vistas para Usuario
class UsuarioCreateView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioListView(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Vistas para CientificoDeDatos
class CientificoDeDatosCreateView(generics.CreateAPIView):
    queryset = CientificoDeDatos.objects.all()
    serializer_class = CientificoDeDatosSerializer

class CientificoDeDatosListView(generics.ListAPIView):
    queryset = CientificoDeDatos.objects.all()
    serializer_class = CientificoDeDatosSerializer

class CientificoDeDatosDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CientificoDeDatos.objects.all()
    serializer_class = CientificoDeDatosSerializer

# Vistas para Agricultor
class AgricultorCreateView(generics.CreateAPIView):
    queryset = Agricultor.objects.all()
    serializer_class = AgricultorSerializer

class AgricultorListView(generics.ListAPIView):
    queryset = Agricultor.objects.all()
    serializer_class = AgricultorSerializer

class AgricultorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agricultor.objects.all()
    serializer_class = AgricultorSerializer

# Vistas para Cultivo
class CultivoCreateView(generics.CreateAPIView):
    queryset = Cultivo.objects.all()
    serializer_class = CultivoSerializer

class CultivoListView(generics.ListAPIView):
    queryset = Cultivo.objects.all()
    serializer_class = CultivoSerializer

class CultivoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cultivo.objects.all()
    serializer_class = CultivoSerializer

# Vistas para DatoClimatico
class DatoClimaticoCreateView(generics.CreateAPIView):
    queryset = DatoClimatico.objects.all()
    serializer_class = DatoClimaticoSerializer

class DatoClimaticoListView(generics.ListAPIView):
    queryset = DatoClimatico.objects.all()
    serializer_class = DatoClimaticoSerializer

class DatoClimaticoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DatoClimatico.objects.all()
    serializer_class = DatoClimaticoSerializer

# Vistas para ModeloPredictivo
class ModeloPredictivoCreateView(generics.CreateAPIView):
    queryset = ModeloPredictivo.objects.all()
    serializer_class = ModeloPredictivoSerializer

class ModeloPredictivoListView(generics.ListAPIView):
    queryset = ModeloPredictivo.objects.all()
    serializer_class = ModeloPredictivoSerializer

class ModeloPredictivoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ModeloPredictivo.objects.all()
    serializer_class = ModeloPredictivoSerializer

# Vistas para Alerta
class AlertaCreateView(generics.CreateAPIView):
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer

class AlertaListView(generics.ListAPIView):
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer

class AlertaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer

# Vistas para Recomendacion
class RecomendacionCreateView(generics.CreateAPIView):
    queryset = Recomendacion.objects.all()
    serializer_class = RecomendacionSerializer

class RecomendacionListView(generics.ListAPIView):
    queryset = Recomendacion.objects.all()
    serializer_class = RecomendacionSerializer

class RecomendacionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recomendacion.objects.all()
    serializer_class = RecomendacionSerializer