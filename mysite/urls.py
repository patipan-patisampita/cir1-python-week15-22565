from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/',include('book_management.urls'))
    path('book_management/',include('book_management.urls'))
]
