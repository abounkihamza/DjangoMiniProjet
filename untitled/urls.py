from django.contrib import admin
from django.urls import path,include
from MiniProjetDjango.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('medicaments/',medicament_list),
    path('medicaments/<int:pk>',medicament_detail),
    path('fournisseurs/',fournisseur_list),
    path('fournisseurs/<int:pk>', fournisseur_detail),
]
