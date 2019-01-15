from django.conf.urls import url

from .views import HomeView, CrearListaView, TareasView, TerminarTareaView, cerrar_sesion

app_name = 'todo_list_app'

urlpatterns = [
    url(r'^inicio/$', HomeView.as_view(), name='inicio'),
    url(r'^crear_lista/$', CrearListaView.as_view(), name='crear_lista'),
    url(r'^lista_tareas/$', TareasView.as_view(), name='lista_tareas'),
    url(r'^terminar_tarea/$', TerminarTareaView.as_view(), name='terminar_tarea'),
    url(r'^cerrar_sesion/$', cerrar_sesion, name='cerrar_sesion'),
]
