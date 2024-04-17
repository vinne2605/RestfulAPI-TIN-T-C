from django.contrib import admin
from django.urls import path
from api_tintuc.views import gd_list, gd_detail,tt_list,tt_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('giaidau/', gd_list),
    path('giaidau/<int:pk>/', gd_detail),
    path('tintuc/', tt_list),
    path('tintuc/<int:pk>/', tt_detail),
]

