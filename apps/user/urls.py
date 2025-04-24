from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.urls import path
from drf_yasg import openapi
from .views import ( 
    IndexView,
    RegisterView, 
    LoginView, 
    LogoutView, 
    PasswordResetView, 
    ResetNewPasswordView, 
    CheckVerifyCodeView, 
)

schema_view = get_schema_view(
    openapi.Info(
        title="Rest Api",
        default_version='v1',
        description="API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="claymrx571@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

app_name = 'accounts'
urlpatterns += [
    path('', IndexView.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reset-password/', PasswordResetView.as_view(), name='password-reset'),
    path('reset-new-password/<uuid:uuid>/', ResetNewPasswordView.as_view(), name='reset-new-password'),
    path('check-verify-email/<uuid:uuid>/', CheckVerifyCodeView.as_view(), name='check-verify-code'),
]
