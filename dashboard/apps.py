from django.apps import AppConfig
from . import signals

class DashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'
    
    
    #call the signals
    
    def ready(self):
        
   
        
        import dashboard.signals
        