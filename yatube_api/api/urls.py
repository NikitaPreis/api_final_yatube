from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter() 

router.register(r'v1/posts', PostViewSet, basename='post')
router.register(r'v1/groups', GroupViewSet, basename='group')
router.register(r'^v1/posts/(?P<post_id>[^/.]+)/comments',
                CommentViewSet, basename='comment')
router.register(r'v1/follow', FollowViewSet, basename='follow')

app_name = 'api'

urlpatterns = [
    path('v1/auth/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
