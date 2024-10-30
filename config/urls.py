from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="My Django API",
        default_version='v1',
        description="API documentation for managing brands, payments, bookings, and user accounts.",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="support@yourapp.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('datetimeapp.urls')),
    path('brand/', include('brands.urls')),
    path('payment/', include('payment.urls')),
    path('booking/', include('booking.urls')),
    path('account/', include('registeraccount.urls')),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
