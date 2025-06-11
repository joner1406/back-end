from django.urls import path
from .views import (
    UsuarioListView,
    UsuarioDetailView,
    CientificoDeDatosListView,
    CientificoDeDatosDetailView,
    AgricultorListView,
    AgricultorDetailView,
    CultivoListView,
    CultivoDetailView,
    DatoClimaticoListView,
    DatoClimaticoDetailView,
    ModeloPredictivoListView,
    ModeloPredictivoDetailView,
    AlertaListView,
    AlertaDetailView
)
urlpatterns = [
    # Rutas para Usuario
    path('usuarios/', UsuarioListView.as_view(), name='usuario'),
    # Rutas para CientificoDeDatos
    path('cientificos/', CientificoDeDatosListView.as_view(), name='cientifico'),
    # Rutas para Agricultor
    path('agricultores/', AgricultorListView.as_view(), name='agricultor'),
    # Rutas para Cultivo
    path('cultivos/', CultivoListView.as_view(), name='cultivo'),
    # Rutas para DatoClimatico
    path('datos-climaticos/', DatoClimaticoListView.as_view(), name='dato-climatico'),
    # Rutas para ModeloPredictivo
    path('modelos-predictivos/', ModeloPredictivoListView.as_view(), name='modelo-predictivo'),
    # Rutas para Alerta
    path('alertas/', AlertaListView.as_view(), name='alerta'),
]