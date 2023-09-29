
from django.contrib import admin
from django.urls import path
from reserva.views import Cadastrar, Deletar, Listar, Editar,  Index ,Detalhar
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

] + static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)