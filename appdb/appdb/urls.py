from django.urls import path
from django.contrib import admin
from django.http import HttpResponseRedirect


def redirect(request):
    return HttpResponseRedirect("/admin/")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", redirect),
]
