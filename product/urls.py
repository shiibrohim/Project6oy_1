from django.urls import path
from .views import home, contact, about, ProductListView, ProductDetailView, ProductUpdateView, ProductDeleteView, ProductCreateView, contact_list


urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('products/', ProductListView.as_view(), name='list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='details'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete'),
    path('products/create/', ProductCreateView.as_view(), name='create'),
    path('contact_list/', contact_list, name='contact_list'),




]