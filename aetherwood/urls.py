from django.contrib import admin
from django.urls import path
from estudio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('editar/<int:id>/', views.editar, name='editar'),
]