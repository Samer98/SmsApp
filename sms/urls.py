from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('campaign', views.SmsCampaign, basename='sms-files')
#
urlpatterns = router.urls
#
# urlpatterns = [
#     path("file/",views.SmsFileViewSet.as_view())
# ]