from django.urls import path
from rest_framework.routers import DefaultRouter

from materials.apps import MaterialsConfig
from materials.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, SubscriptionCreateAPIView, SubscriptionListAPIView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>', LessonRetrieveAPIView.as_view(), name='lesson-detail'),
    path('lesson/update/<int:pk>', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>', LessonDestroyAPIView.as_view(), name='lesson-delete'),
    path('subs/create/', SubscriptionCreateAPIView.as_view(), name='subs_create'),
    path('subs/', SubscriptionListAPIView.as_view(), name='subs'),
]

urlpatterns += router.urls
