
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('pages.urls', namespace='pages')),
    path('blogs/', include('blogs.urls', namespace='blogs')),
    path('products/', include('products.urls', namespace='products')),
    path('about/', include('pages.urls', namespace='about')),
    path('shop/', include('pages.urls', namespace='shop')),
    path('checkout/', include('users.urls', namespace='checkout')),
    path('register/', include('users.urls', namespace='register')),
    path('login/', include('users.urls', namespace='login')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
