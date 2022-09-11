from django.urls import path, include

import pawpals

from django.contrib import admin
from ..pawpals import views

urlpattern = [
    path('', include(pawpals.urls)),
    path("admin/", admin.site.urls),

]   