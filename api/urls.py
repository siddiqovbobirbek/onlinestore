from django.urls import path

from .views import ProductAPIView, ProductDetailAPIView


urlpatterns = [
    path('', ProductAPIView.as_view()),
    path('<int:pk>/', ProductDetailAPIView.as_view()),

]