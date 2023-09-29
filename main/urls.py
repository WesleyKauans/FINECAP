
from django.contrib import admin
from django.urls import path
from reserva.views import Cadastrar, Deletar, Listar, Editar,  Index ,Detalhar
from stand.views import Cadastrar_S, Deletar_S, Listar_S, Editar_S

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(),name='index'),
    path('form/', Cadastrar.as_view(),name='cadastrar'),
    path('listar/', Listar.as_view(),name='listar'),
    path('editar/<int:pk>/', Editar.as_view(), name='editar'),
    path('apagar/<int:pk>/',Deletar.as_view(), name='apagar'),
    path('detalhar/<int:pk>/', Detalhar.as_view(), name='detalhar'),

    path('form/', Cadastrar_S.as_view(),name='cadastrar_s'),
    path('listar/', Listar_S.as_view(),name='listar_s'),
    path('editar/<int:pk>/', Editar_S.as_view(), name='editar_s'),
    path('apagar/<int:pk>/',Deletar_S.as_view(), name='apagar_s'),

] + static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)