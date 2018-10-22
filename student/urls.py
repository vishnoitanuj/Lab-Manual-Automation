from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
	url(r'^student/(?P<pk>\d+)$', views.UserProfileDetailView.as_view(), name='student-detail'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
