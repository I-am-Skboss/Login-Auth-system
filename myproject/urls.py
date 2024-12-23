from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.http import HttpResponse
from django.views.generic import RedirectView

@login_required
def home_view(request):
    return HttpResponse('<h1>Welcome to the Home Page</h1>')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Include accounts URLs
    path('', include('accounts.urls')),  # Default redirect to accounts
]