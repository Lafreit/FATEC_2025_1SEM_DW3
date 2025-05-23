from django.urls import path
from . import views
from .views import FeriadoDetailView, FeriadoListCreateView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('',views.feriado),
    path('listar_feriados/', views.listar_feriados, name='listar_feriados'),
    path('adicionar_novos_feriados/', views.adicionar_feriado, name='add_feriado'),
    path('feriados/<int:feriado_id>/deletar/', views.deletar_feriado, name='deletar_feriado'),
    path('feriados/<int:feriado_id>/atualizar/', views.atualizar_feriado, name='atualizar_feriado'),
    path('json_all_feriados', views.listar_feriados_json),
    path('api/feriados/', FeriadoListCreateView.as_view(), name='api_feriados_list_create'),
    path('api/feriados/<int:pk>/', FeriadoDetailView.as_view(), name='api_feriados_detail'),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]
