from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import about, contact, home, footer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', contact, name='contact_us'),
    path('footer/', footer, name='footer'),
    path('about/', about, name='about_us'),
    path('', home, name='home'),

    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('meals/', include('meals.urls', namespace='meals')),
    path('cart/', include('carts.urls', namespace='cart')),
    path('order/', include('order.urls', namespace='order')),
    path('users/', include('user.urls', namespace='user')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
