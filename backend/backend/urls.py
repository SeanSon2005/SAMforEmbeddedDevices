from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import ServeProtectedMedia, ServeAnnotatedMedia

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("profiles.urls")),
    path("protected_media/<int:user_id>/<int:dataset_id>/<str:filename>", ServeProtectedMedia.as_view(), name="serve_protected_media"),
    path("protected_media/training/<int:user_id>/<int:dataset_id>/<int:training_id>/annotated_images/<str:filename>", ServeAnnotatedMedia.as_view(), name="serve_annotated_media"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
