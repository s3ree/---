from django.urls import path
from .views import book_kitchen, personal_info, success_page, user_bookings
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('personal-info/', personal_info, name='personal_info'),
    path('book-kitchen/', book_kitchen, name='book_kitchen'),
    path('success/', success_page, name='success'),
    path('my_bookings/', user_bookings, name='user_bookings'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)