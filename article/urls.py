from rest_framework.routers import DefaultRouter

from .views import ArticleViewSet


router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='user')

urlpatterns = router.urls