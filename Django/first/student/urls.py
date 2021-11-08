from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import hotel_image_view
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.form_profile.as_view(), name='profile'),
    # path('image_upload/', hotel_image_view, name='image_upload'),
    path('image_upload/', views.hotel_image_view.as_view(), name='image_upload'),
    path('profile_api/', views.ProfileAPI.as_view(), name='profileAPI'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
