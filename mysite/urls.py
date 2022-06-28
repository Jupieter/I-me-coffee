from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home_page, contact_page, view_modal_mess, proba



app_name = 'mysite'

urlpatterns = [
    path('proba', proba, name="proba"),
    path('admin/', admin.site.urls),
    path('', home_page, name="home_url"),
    path('shop/', include('shop.urls', namespace='shop')),
    path('contact/', contact_page, name='contact_page'),
    path('accounts/', include('accounts.urls')),
    path('raw_material/', include('raw_material.urls')),
    
    # path('addresses/', include('addresses.urls')),
    # path('cart/', include('carts.urls')),
    # path('search/', include('search.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

htmx_patterns = [
    path('modal_mess/', view_modal_mess, name='view_modal_mess'),
]

urlpatterns += htmx_patterns