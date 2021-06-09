from rest_framework import routers

from .views import BookView, AuthorView, FindView, GenreView


router = routers.SimpleRouter()
router.register(r'books', BookView)
router.register(r'authors', AuthorView)
router.register(r'find_by_authors', FindView)
router.register(r'genres', GenreView)

urlpatterns = router.urls
