
from django.contrib import admin
from django.urls import path, include
from employee.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employee.urls')),
    # path('employee/', include('employee_management.urls')),  # Removed to fix recursion error
]
