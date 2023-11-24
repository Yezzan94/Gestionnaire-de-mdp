from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mots_de_passe/', include('gestion_mdp.urls')),
    path('', RedirectView.as_view(url='/mots_de_passe/')),
]
