from django.contrib import admin
from django.urls import path, include
from reserva.views import Cadastrar, Deletar, Listar, Editar,  Index ,Detalhar, Add, Index2, Detalhar2, Listar2
from stand.views import Cadastrar_S, Deletar_S, Listar_S, Editar_S, Detalhar_S, Detalhar_S2, Listar_S2
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("accounts/", include("allauth.urls")),


    path('admin/', admin.site.urls),
    path('', Index.as_view(),name='index'),
    path('i', Index2.as_view(),name='index2'),
    path('add', Add.as_view(),name='add'),


    path('form/', Cadastrar.as_view(),name='cadastrar'),
    path('listar/', Listar.as_view(),name='listar'),
    path('listar2/', Listar2.as_view(),name='listar2'),
    path('editar/<int:pk>/', Editar.as_view(), name='editar'),
    path('apagar/<int:pk>/',Deletar.as_view(), name='apagar'),
    path('detalhar/<int:pk>/', Detalhar.as_view(), name='detalhar'),
    path('detalhar2/<int:pk>/', Detalhar2.as_view(), name='detalhar2'),


    path('form-s/', Cadastrar_S.as_view(),name='cadastrar_s'),
    path('listar-s/', Listar_S.as_view(),name='listar_s'),
    path('listar-s2/', Listar_S2.as_view(),name='listar_s2'),
    path('editar-s/<int:pk>/', Editar_S.as_view(), name='editar_s'),
    path('apagar-s/<int:pk>/',Deletar_S.as_view(), name='apagar_s'),
    path('detalhar-s/<int:pk>/', Detalhar_S.as_view(), name='detalhar_s'),
    path('detalhar-s2/<int:pk>/', Detalhar_S2.as_view(), name='detalhar_s2'),





] + static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)