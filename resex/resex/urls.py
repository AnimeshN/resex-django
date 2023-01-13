from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('labs.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]


admin.site.site_header = "ResEx Administration Page"
admin.site.site_title = "ResEx Administration"
admin.site.index_title = ""