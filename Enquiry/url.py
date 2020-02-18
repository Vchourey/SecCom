from django.urls import path
from Vijayweb import settings
from  django.conf.urls.static import static
from .views import Contact_Enquiry, Thanks

# TEMPLATE URLS!

app_name = 'enquiry'

urlpatterns = [
    path('', Contact_Enquiry, name='contact'),
    path('thanks/', Thanks , name='thanks'),
#    path('', views.index, name='homeyard'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_DIR)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_DIR)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_DIR)
