from django.apps import AppConfig


class {{ cookiecutter.app_config_name }}(AppConfig):
    name = '{{ cookiecutter.app_name }}'

    def ready(self):
        try:
            # pylint: disable=unused-import
            import {{ cookiecutter.app_name }}.signals
        except ImportError:
            pass
