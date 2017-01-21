from django.conf.urls import url, include
from django.contrib import admin
from myapp import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^runcode/$', views.submit, name='submit'),
    url(r'^admin/', admin.site.urls),
]
