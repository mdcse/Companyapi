from api.views import CompanyViewSet, EmployeeViewSet
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)

router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),

]