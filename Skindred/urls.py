from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.conf import settings
# from django.conf.urls.static import static
from django.views.generic import RedirectView
from . import views
from django.conf.urls import url, include

urlpatterns = [
	url(r'admin/', admin.site.urls),
	url(r'accounts/', include('django.contrib.auth.urls')),
	url(r'^logout/', views.logout_view, name='logout'),
	url(r'^main/', views.main,name='main'),
	url(r'^', RedirectView.as_view(pattern_name='main', permanent=False)),
]

urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
