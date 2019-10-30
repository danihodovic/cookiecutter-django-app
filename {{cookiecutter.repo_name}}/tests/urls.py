from django.urls import include, path


urlpatterns = [
    path('', include('{{ cookiecutter.app_name }}.urls', namespace='{{ cookiecutter.app_name }}')),
]
