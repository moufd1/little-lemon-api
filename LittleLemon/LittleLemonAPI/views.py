from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User, Group
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from decimal import Decimal
from datetime import date

from .models import Category, MenuItem, Cart, Order, OrderItem
from .serializers import (
    CategorySerializer, MenuItemSerializer, UserSerializer,
    CartSerializer, OrderSerializer, OrderItemSerializer
)
from .permissions import (
    IsManager, IsManagerOrReadOnly, IsOwnerOrManager, 
    IsDeliveryCrewOrManager, IsCustomer, IsDeliveryCrew
)

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from decimal import Decimal
from datetime import date

from .models import Category, MenuItem, Cart, Order, OrderItem
from .serializers import (
    CategorySerializer, MenuItemSerializer, UserSerializer,
    CartSerializer, OrderSerializer, OrderItemSerializer
)
from .permissions import (
    IsManager, IsManagerOrReadOnly, IsOwnerOrManager, 
    IsDeliveryCrewOrManager, IsCustomer, IsDeliveryCrew
)

def home_view(request):
    """Custom homepage for the Little Lemon API"""
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Little Lemon API</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 0;
                padding: 20px;
                background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
                min-height: 100vh;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            }
            .logo {
                text-align: center;
                font-size: 2.5rem;
                color: #2c3e50;
                margin-bottom: 10px;
            }
            .subtitle {
                text-align: center;
                color: #7f8c8d;
                margin-bottom: 30px;
            }
            .endpoints {
                background: #f8f9fa;
                padding: 20px;
                border-radius: 5px;
                margin: 20px 0;
            }
            .endpoint {
                background: white;
                padding: 10px;
                margin: 10px 0;
                border-left: 4px solid #3498db;
                border-radius: 3px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1 class="logo">🍋 Little Lemon API</h1>
            <p class="subtitle">A comprehensive REST API for the Little Lemon restaurant</p>
            
            <div class="endpoints">
                <h3>Available Endpoints:</h3>
                <div class="endpoint"><strong>GET /api/menu-items/</strong> - View all menu items</div>
                <div class="endpoint"><strong>GET /api/categories/</strong> - View all categories</div>
                <div class="endpoint"><strong>GET /api/cart/menu-items/</strong> - Manage cart items</div>
                <div class="endpoint"><strong>GET /api/orders/</strong> - Manage orders</div>
                <div class="endpoint"><strong>POST /auth/users/</strong> - User registration</div>
                <div class="endpoint"><strong>POST /auth/token/login/</strong> - User login</div>
                <div class="endpoint"><strong>GET /api/groups/manager/users/</strong> - Manager group management</div>
                <div class="endpoint"><strong>GET /api/groups/delivery-crew/users/</strong> - Delivery crew management</div>
            </div>
            
            <p style="text-align: center; color: #7f8c8d; margin-top: 30px;">
                Welcome to the Little Lemon API! Use the endpoints above to interact with our system.
            </p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)

# Categories
class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsManagerOrReadOnly]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

# Menu Items
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsManagerOrReadOnly]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'featured']
    search_fields = ['title', 'category__title']
    ordering_fields = ['price', 'title']
    ordering = ['title']

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsManagerOrReadOnly]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

# Group Management Views
class ManagerGroupView(generics.ListCreateAPIView, generics.DestroyAPIView):
    """Manage users in Manager group"""
    permission_classes = [IsManager]
    serializer_class = UserSerializer
    
    def get_queryset(self):
        manager_group, created = Group.objects.get_or_create(name='Manager')
        return manager_group.user_set.all()
    
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        if not username:
            return Response({'error': 'Username is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(username=username)
            manager_group, created = Group.objects.get_or_create(name='Manager')
            manager_group.user_set.add(user)
            return Response({'message': f'User {username} added to Manager group'}, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        if not user_id:
            return Response({'error': 'User ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(id=user_id)
            manager_group, created = Group.objects.get_or_create(name='Manager')
            manager_group.user_set.remove(user)
            return Response({'message': f'User {user.username} removed from Manager group'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

class DeliveryCrewGroupView(generics.ListCreateAPIView, generics.DestroyAPIView):
    """Manage users in Delivery crew group"""
    permission_classes = [IsManager]
    serializer_class = UserSerializer
    
    def get_queryset(self):
        delivery_group, created = Group.objects.get_or_create(name='Delivery crew')
        return delivery_group.user_set.all()
    
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        if not username:
            return Response({'error': 'Username is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(username=username)
            delivery_group, created = Group.objects.get_or_create(name='Delivery crew')
            delivery_group.user_set.add(user)
            return Response({'message': f'User {username} added to Delivery crew group'}, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        if not user_id:
            return Response({'error': 'User ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(id=user_id)
            delivery_group, created = Group.objects.get_or_create(name='Delivery crew')
            delivery_group.user_set.remove(user)
            return Response({'message': f'User {user.username} removed from Delivery crew group'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

# Cart Views
class CartView(generics.ListCreateAPIView, generics.DestroyAPIView):
    """Customer cart management"""
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated, IsCustomer]
    
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def delete(self, request, *args, **kwargs):
        """Clear all cart items for the current user"""
        Cart.objects.filter(user=request.user).delete()
        return Response({'message': 'Cart cleared'}, status=status.HTTP_200_OK)

# Order Views
class OrderView(generics.ListCreateAPIView):
    """Handle orders for customers and managers"""
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'delivery_crew']
    search_fields = ['status']
    ordering_fields = ['date', 'total']
    ordering = ['-date']
    
    def get_queryset(self):
        if self.request.user.groups.filter(name='Manager').exists():
            return Order.objects.all()
        elif self.request.user.groups.filter(name='Delivery crew').exists():
            return Order.objects.filter(delivery_crew=self.request.user)
        else:
            return Order.objects.filter(user=self.request.user)
    
    def create(self, request, *args, **kwargs):
        # Only customers can create orders
        if request.user.groups.filter(name__in=['Manager', 'Delivery crew']).exists():
            return Response({'error': 'Only customers can create orders'}, status=status.HTTP_403_FORBIDDEN)
        
        # Create order from cart items
        cart_items = Cart.objects.filter(user=request.user)
        if not cart_items.exists():
            return Response({'error': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)
        
        total = sum(item.price for item in cart_items)
        order = Order.objects.create(
            user=request.user, 
            total=total, 
            date=date.today(),
            status=False
        )
        
        # Create order items from cart
        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                menuitem=cart_item.menuitem,
                quantity=cart_item.quantity,
                unit_price=cart_item.unit_price,
                price=cart_item.price
            )
        
        # Clear cart
        cart_items.delete()
        
        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SingleOrderView(generics.RetrieveUpdateAPIView):
    """Handle single order operations"""
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.groups.filter(name='Manager').exists():
            return Order.objects.all()
        elif self.request.user.groups.filter(name='Delivery crew').exists():
            return Order.objects.filter(delivery_crew=self.request.user)
        else:
            return Order.objects.filter(user=self.request.user)
    
    def update(self, request, *args, **kwargs):
        order = self.get_object()
        
        if request.user.groups.filter(name='Manager').exists():
            # Managers can update delivery_crew and status
            return super().update(request, *args, **kwargs)
        elif request.user.groups.filter(name='Delivery crew').exists():
            # Delivery crew can only update status
            if 'status' in request.data and len(request.data) == 1:
                order.status = request.data['status']
                order.save()
                serializer = self.get_serializer(order)
                return Response(serializer.data)
            else:
                return Response({'error': 'Delivery crew can only update status'}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({'error': 'Customers cannot update orders'}, status=status.HTTP_403_FORBIDDEN)