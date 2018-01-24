from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.routers import DefaultRouter
from .viewsets.usercsv_viewset import UserCSVViewSet, UserCSVSearchView, UserCSVExportView,uploadCSV


router = DefaultRouter()
router.register(prefix='mobile', viewset=UserCSVViewSet)
urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^api/', include(router.urls)),
                  url(r'^api/search$', UserCSVSearchView.as_view()),
                  url(r'^api/exportcsv$', UserCSVExportView.as_view()),
                  url(r'^api/upload$', uploadCSV ),

              ]
