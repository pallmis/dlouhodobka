from django.urls import path, include
from .views import RecipeViewSet, login, register
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("recipes/<int:pk>/", RecipeViewSet.as_view({"get": "retrieve"}), name="recipe-detail"),
    path("user/login/", login, name="login"),
    path("user/register/", register, name="register"),
]