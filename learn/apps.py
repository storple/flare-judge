from django.apps import AppConfig

class LearnConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'learn'
    
    #registers needed signals
    def ready(self):
        from . import signals
