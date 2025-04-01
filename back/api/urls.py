from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenBlacklistView)
from .views import listar_ambientes, listar_gestores, listar_historico, listar_manutentores, listar_OrdemServico, listar_patrimonios, listar_responsaveis
from .views import AmbientesView, GestoresView, HistoricoView, ManutentoresView, OrdemServicoView, PatrimoniosView, ResponsaveisView
from .views import AmbientesDetailView, GestoresDetailView, HistoricoDetailView, ManutentoresDetailView, OrdemServicoDetailView, PatrimoniosDetailView, ResponsaveisDetailView
from .views import AmbientesSearchView, GestoresSearchView, HistoricoSearchView, ManutentoresSearchView, OrdemServicoSearchView, PatrimoniosSearchView, ResponsaveisSearchView


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'),

    path('ambientes', listar_ambientes),
    path('ambi', AmbientesView.as_view()),
    path('ambi/id/<int:pk>', AmbientesDetailView.as_view()),
    path('ambientes/search/', AmbientesSearchView.as_view()),

    path('gestores', listar_gestores),
    path('gest', GestoresView.as_view()),
    path('gest/id/<int:pk>', GestoresDetailView.as_view()),
    path('gestores/search/', GestoresSearchView.as_view()),

    path('historico', listar_historico),
    path('hist', HistoricoView.as_view()),
    path('hist/id/<int:pk>', HistoricoDetailView.as_view()),
    path('historico/search/', HistoricoSearchView.as_view()),

    path('manutentores', listar_manutentores),
    path('manutent', ManutentoresView.as_view()),
    path('manutent/id/<int:pk>', ManutentoresDetailView.as_view()),
    path('manutentores/search/', ManutentoresSearchView.as_view()),

    path('ordemServico', listar_OrdemServico),
    path('ordemServ', OrdemServicoView.as_view()),
    path('ordemServ/id/<int:pk>', OrdemServicoDetailView.as_view()),
    path('ordemServico/search/', OrdemServicoSearchView.as_view()),

    path('patrimonio', listar_patrimonios),
    path('patri', PatrimoniosView.as_view()),
    path('patri/id/<int:pk>', PatrimoniosDetailView.as_view()),
    path('patrimonio/search/', PatrimoniosSearchView.as_view()),

    path('responsaveis', listar_responsaveis),
    path('responsa', ResponsaveisView.as_view()),
    path('responsa/id/<int:pk>', ResponsaveisDetailView.as_view()),
    path('responsaveis/search/', ResponsaveisSearchView.as_view()),
]