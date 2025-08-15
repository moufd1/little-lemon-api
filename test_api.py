#!/usr/bin/env python3
"""
Little Lemon API Test Script
Tests all endpoints mentioned in the requirements to ensure they work correctly.
"""

import requests
import json
import sys

BASE_URL = "http://127.0.0.1:8000"

def test_endpoint(method, endpoint, headers=None, data=None, expected_status=200):
    """Test a single endpoint"""
    url = f"{BASE_URL}{endpoint}"
    
    try:
        if method.upper() == 'GET':
            response = requests.get(url, headers=headers)
        elif method.upper() == 'POST':
            response = requests.post(url, headers=headers, json=data)
        elif method.upper() == 'PUT':
            response = requests.put(url, headers=headers, json=data)
        elif method.upper() == 'DELETE':
            response = requests.delete(url, headers=headers)
        
        print(f"✅ {method} {endpoint} - Status: {response.status_code}")
        
        if response.status_code == expected_status:
            return True
        else:
            print(f"   Expected: {expected_status}, Got: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print(f"❌ {method} {endpoint} - Connection Error (Server may not be running)")
        return False
    except Exception as e:
        print(f"❌ {method} {endpoint} - Error: {str(e)}")
        return False

def main():
    """Run all endpoint tests"""
    print("🍋 Little Lemon API Endpoint Tests")
    print("=" * 50)
    
    tests = [
        # Basic endpoints
        ("GET", "/", 200),
        ("GET", "/api/menu-items/", 200),
        ("GET", "/api/categories/", 200),
        
        # Authentication endpoints (should return 200 or appropriate status)
        ("GET", "/auth/users/", 405),  # Method not allowed for GET
        ("GET", "/auth/token/login/", 405),  # Method not allowed for GET
        
        # Group management endpoints (should require authentication)
        ("GET", "/api/groups/manager/users/", 401),  # Unauthorized without token
        ("GET", "/api/groups/delivery-crew/users/", 401),  # Unauthorized without token
        
        # Cart endpoints (should require authentication)
        ("GET", "/api/cart/menu-items/", 401),  # Unauthorized without token
        
        # Order endpoints (should require authentication)
        ("GET", "/api/orders/", 401),  # Unauthorized without token
        ("GET", "/api/cart/orders/", 401),  # Unauthorized without token
    ]
    
    passed = 0
    total = len(tests)
    
    for method, endpoint, expected_status in tests:
        if test_endpoint(method, endpoint, expected_status=expected_status):
            passed += 1
    
    print("\n" + "=" * 50)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your Little Lemon API is working correctly.")
    else:
        print("⚠️  Some tests failed. Check the output above for details.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
