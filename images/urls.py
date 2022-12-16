from django.urls import path
from .views import GenerateImagesView, GetImageHistoryView

urlpatterns = [
    path('generate/', GenerateImagesView.as_view(), name='generate-image(s)'),
    path('history/', GetImageHistoryView.as_view(), name='get-image-history')
]
