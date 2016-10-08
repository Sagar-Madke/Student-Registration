from django.conf.urls import url
from django.contrib import admin
from registrationapp import views
from . import views

urlpatterns = [
	url(r'^$', views.index, name = "index"),
	url(r'^registration/$', views.register, name = "register"),
    url(r'^admin/', admin.site.urls),
]



