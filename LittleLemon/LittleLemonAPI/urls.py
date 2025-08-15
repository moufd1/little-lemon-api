from django.urls import path
from . import views

urlpatterns = [
    # Menu items
    path('menu-items/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-item-detail'),
    
    # Categories
    path('categories/', views.CategoriesView.as_view(), name='categories'),
    
    # Groups management
    path('groups/manager/users/', views.ManagerGroupView.as_view(), name='manager-group'),
    path('groups/manager/users/<int:pk>/', views.ManagerGroupView.as_view(), name='manager-group-detail'),
    path('groups/delivery-crew/users/', views.DeliveryCrewGroupView.as_view(), name='delivery-crew-group'),
    path('groups/delivery-crew/users/<int:pk>/', views.DeliveryCrewGroupView.as_view(), name='delivery-crew-group-detail'),
    
    # Cart management
    path('cart/menu-items/', views.CartView.as_view(), name='cart'),
    
    # Orders - both /api/orders and /api/cart/orders for compatibility
    path('orders/', views.OrderView.as_view(), name='orders'),
    path('orders/<int:pk>/', views.SingleOrderView.as_view(), name='order-detail'),
    path('cart/orders/', views.OrderView.as_view(), name='cart-orders'),  # Alias for tests
    path('cart/orders/<int:pk>/', views.SingleOrderView.as_view(), name='cart-order-detail'),  # Alias for tests
]