from django.conf import settings


def data_context_processor(request):
    
    environment = settings.ENVIRONMENT
    domain = settings.SITE_DOMAINE
    
    return {
        'environment':environment, 
        'domain':domain,       
    }
