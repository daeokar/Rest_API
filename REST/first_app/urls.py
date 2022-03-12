from rest_framework.routers import DefaultRouter, SimpleRouter
from first_app.views import StudentViewSet, StudentModelViewSet, CollegeModelViewSet, AlbumModelViewSet, TrackModelViewSet

router = DefaultRouter()

router.register(r'studen-op', StudentModelViewSet, basename='student')  # urls -- CRUD  -- 
router.register(r'college-op', CollegeModelViewSet, basename='college')


router.register(r'albums', AlbumModelViewSet, basename='album')
router.register(r'tracks', TrackModelViewSet, basename='track')


# for i in router.urls:
#     print(i)

# <URLPattern '^studen-op/$' [name='student-list']>  # create
# <URLPattern '^studen-op\.(?P<format>[a-z0-9]+)/?$' [name='student-list']>  # ?format=api
# <URLPattern '^studen-op/(?P<pk>[^/.]+)/$' [name='student-detail']>   # get, update, patch
# <URLPattern '^studen-op/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$' [name='student-detail']>
# <URLPattern '^$' [name='api-root']>
# <URLPattern '^\.(?P<format>[a-z0-9]+)/?$' [name='api-root']>