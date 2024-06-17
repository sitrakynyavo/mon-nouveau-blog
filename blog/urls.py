from django.urls import path
from . import views
#import de la fonction path et les vues liées à notre application blog

urlpatterns = [
    #indiquer la première vue (page) à afficher lorsque l'on se navigue sur l'URL
    path('', views.post_list, name='post_list'),
]