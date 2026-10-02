from django.contrib import admin
from django.urls import path
from estudio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rutas Públicas (El sitio web que verá el cliente)
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('galeria/', views.galeria, name='galeria'),
    path('contacto/', views.contacto, name='contacto'),
    
    # Rutas Privadas (Movimos el login aquí para que no sea la página de inicio)
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('editar/<int:id>/', views.editar, name='editar'),
]