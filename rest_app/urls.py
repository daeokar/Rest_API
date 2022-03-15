
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_app.views import *

router = SimpleRouter()

# router.register(r'studen-op', StudentViewset, basename='student')  # ----urls -- CRUD  -- 
router.register(r'studen-op', StudentModelViewset, basename='student')
# router.register(r'studen-op', StudentReadOnlyModelViewset, basename='student')   #----we can only read tha data 

#----collage urls
router.register(r'collage-op', CollageModelViewset, basename='collage')


# for i in router.urls:
#     print(i)

# <URLPattern '^studen-op/$' [name='student-list']>
# <URLPattern '^studen-op\.(?P<format>[a-z0-9]+)/?$' [name='student-list']>
# <URLPattern '^studen-op/(?P<pk>[^/.]+)/$' [name='student-detail']>
# <URLPattern '^studen-op/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$' [name='student-detail']>
# <URLPattern '^$' [name='api-root']>
# <URLPattern '^\.(?P<format>[a-z0-9]+)/?$' [name='api-root']>



