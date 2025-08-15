# 🍋 Little Lemon Restaurant API

## 📌 Introduction
This project is a fully functional REST API for the Little Lemon Restaurant, allowing client developers to build web and mobile applications for menu management, order processing, and user role management.

Built with Django and Django REST Framework, using Pipenv for dependency management.

##  Project Structure
- **Single Django App**: `LittleLemonAPI`
- All API endpoints are implemented within this app.
- Dependencies managed with Pipenv (`Pipfile` & `Pipfile.lock`).
- Supports both function-based and class-based views.
- Proper naming conventions and status codes are used.

## 👥 User Roles
- **Manager** – Full control over menu items, orders, and group assignments.
- **Delivery Crew** – Assigned to deliver orders and update delivery status.
- **Customer (default)** – Can browse the menu, manage their cart, and place orders.

## 🔑 Authentication & Authorization
- Implemented using **Djoser** for user registration, login, and token generation.
- Permissions enforced according to user roles.
- Secure endpoints with proper HTTP status codes for errors.

## 📜 HTTP Status Codes
| Code | Meaning |
|------|---------|
| 200  | OK – Successful GET, PUT, PATCH, DELETE |
| 201  | Created – Successful POST |
| 401  | Forbidden – Authentication failed |
| 403  | Unauthorized – Authorization failed |
| 400  | Bad Request – Validation errors |
| 404  | Not Found – Resource does not exist |

## 🚀 API Endpoints

### 1. User Registration & Token
| Endpoint | Role | Method | Purpose |
|----------|------|--------|---------|
| `/api/users` | None | POST | Register a new user |
| `/api/users/me/` | Authenticated | GET | Get current user |
| `/token/login/` | None | POST | Generate auth token |

### 2. Menu Items
| Endpoint | Role | Method | Purpose |
|----------|------|--------|---------|
| `/api/menu-items/` | Customer, Delivery Crew | GET | List menu items |
| `/api/menu-items/{id}/` | Customer, Delivery Crew | GET | View single item |
| `/api/menu-items/` | Manager | POST | Add new menu item |
| `/api/menu-items/{id}/` | Manager | PUT/PATCH | Update menu item |
| `/api/menu-items/{id}/` | Manager | DELETE | Delete menu item |

### 3. User Group Management
| Endpoint | Role | Method | Purpose |
|----------|------|--------|---------|
| `/api/groups/manager/users/` | Manager | GET | List managers |
| `/api/groups/manager/users/` | Manager | POST | Add user to manager group |
| `/api/groups/manager/users/{userId}/` | Manager | DELETE | Remove user from manager group |
| `/api/groups/delivery-crew/users/` | Manager | GET | List delivery crew |
| `/api/groups/delivery-crew/users/` | Manager | POST | Add user to delivery crew group |
| `/api/groups/delivery-crew/users/{userId}/` | Manager | DELETE | Remove user from delivery crew group |

### 4. Cart Management
| Endpoint | Role | Method | Purpose |
|----------|------|--------|---------|
| `/api/cart/menu-items/` | Customer | GET | View cart |
| `/api/cart/menu-items/` | Customer | POST | Add item to cart |
| `/api/cart/menu-items/` | Customer | DELETE | Clear cart |

### 5. Orders
| Endpoint | Role | Method | Purpose |
|----------|------|--------|---------|
| `/api/orders/` | Customer | GET | List user's orders |
| `/api/orders/` | Customer | POST | Create new order from cart |
| `/api/orders/{id}/` | Customer | GET | View order details |
| `/api/orders/` | Manager | GET | List all orders |
| `/api/orders/{id}/` | Manager | PUT/PATCH | Assign delivery crew / update status |
| `/api/orders/{id}/` | Manager | DELETE | Delete order |
| `/api/orders/` | Delivery Crew | GET | List assigned orders |
| `/api/orders/{id}/` | Delivery Crew | PATCH | Update delivery status |

## 🔍 Additional Features
- **Filtering, Pagination, Sorting** for `/api/menu-items/` and `/api/orders/`
- **Throttling** for authenticated and anonymous users
- **Proper error handling** with descriptive messages

## 🛠️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/moufd1/little-lemon-api.git
cd little-lemon-api
```

### 2. Install dependencies
```bash
pipenv install
```

### 3. Activate virtual environment
```bash
pipenv shell
```

### 4. Run migrations
```bash
cd LittleLemon
python manage.py makemigrations
python manage.py migrate
```

### 5. Create sample data (optional)
```bash
python manage.py create_sample_data
python manage.py create_test_users
```

### 6. Create superuser
```bash
python manage.py createsuperuser
```

### 7. Run the development server
```bash
python manage.py runserver
```

### Quick Start (Alternative)
You can also use the provided scripts:
```bash
# PowerShell
.\start-server.ps1

# Batch
start.bat
```

## 🌐 Access Points
- **Homepage**: http://127.0.0.1:8000/
- **API Root**: http://127.0.0.1:8000/api/
- **Admin Panel**: http://127.0.0.1:8000/admin/
- **Menu Items**: http://127.0.0.1:8000/api/menu-items/
- **Categories**: http://127.0.0.1:8000/api/categories/

## 📊 Test Credentials
- **Admin**: `admin` / `password123`
- **Manager**: `manager` / `password123`
- **Customer**: `customer` / `password123`
- **Delivery**: `delivery` / `password123`

## 🧪 Testing
Test the API functionality:
```bash
python test_all_endpoints.py
```

## 🔧 Environment Variables
Copy `.env.example` to `.env` and configure your settings:
```bash
cp .env.example .env
```

## 📝 Requirements
- Python 3.12+
- Django 5.2+
- Django REST Framework
- Djoser
- django-filter

## 🚀 Features Implemented
- ✅ User authentication and authorization
- ✅ Token-based authentication
- ✅ Role-based permissions (Manager, Delivery Crew, Customer)
- ✅ Complete CRUD operations for menu items
- ✅ Shopping cart functionality
- ✅ Order management system
- ✅ User group management
- ✅ Filtering, searching, and sorting
- ✅ Pagination
- ✅ Rate limiting/throttling
- ✅ Proper error handling
- ✅ API documentation

## 📈 Project Status
This project implements all required features for a restaurant API including menu management, user authentication, cart functionality, and order processing with proper permissions and error handling.

Une API REST complète pour le restaurant Little Lemon, construite avec Django et Django REST Framework.

## 🚀 Installation et Configuration

### Prérequis
- Python 3.12+
- pipenv

### Instructions d'installation

1. **Cloner le repository et naviguer vers le projet**
   ```bash
   cd C:\Users\TRETEC\Desktop\little-lemon-api\LittleLemon
   ```

2. **Installer les dépendances**
   ```bash
   pipenv install
   ```

3. **Activer l'environnement virtuel**
   ```bash
   pipenv shell
   ```

4. **Lancer les migrations (déjà fait)**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Créer les groupes d'utilisateurs (déjà fait)**
   ```bash
   python manage.py create_groups
   ```

6. **Peupler la base de données avec des données de test (déjà fait)**
   ```bash
   python manage.py populate_data
   ```

7. **Créer les utilisateurs de test (déjà fait)**
   ```bash
   python manage.py create_test_users
   ```

8. **Démarrer le serveur**
   ```bash
   python manage.py runserver
   ```

## 👥 Comptes de Test

### Superuser (Admin)
- **Username:** admin
- **Password:** admin123456

### Manager
- **Username:** manager1
- **Password:** manager123

### Delivery Crew
- **Username:** delivery1
- **Password:** delivery123

### Customers
- **Username:** customer1 / customer2
- **Password:** customer123

## 🔗 Endpoints API

### Authentification
- `POST /auth/users/` - Créer un utilisateur
- `POST /auth/token/login/` - Obtenir un token d'authentification
- `POST /auth/token/logout/` - Se déconnecter

### Menu Items
- `GET /api/menu-items/` - Lister tous les articles de menu
- `POST /api/menu-items/` - Créer un nouvel article (managers seulement)
- `GET /api/menu-items/{id}/` - Détails d'un article spécifique
- `PUT/PATCH /api/menu-items/{id}/` - Modifier un article (managers seulement)
- `DELETE /api/menu-items/{id}/` - Supprimer un article (managers seulement)

### Categories
- `GET /api/categories/` - Lister toutes les catégories
- `POST /api/categories/` - Créer une nouvelle catégorie (managers seulement)

### Gestion des Groupes d'Utilisateurs
- `GET /api/groups/manager/users/` - Lister les managers
- `POST /api/groups/manager/users/` - Ajouter un utilisateur au groupe manager
- `DELETE /api/groups/manager/users/{userId}/` - Retirer un utilisateur du groupe manager
- `GET /api/groups/delivery-crew/users/` - Lister l'équipe de livraison
- `POST /api/groups/delivery-crew/users/` - Ajouter un utilisateur à l'équipe de livraison
- `DELETE /api/groups/delivery-crew/users/{userId}/` - Retirer un utilisateur de l'équipe de livraison

### Panier
- `GET /api/cart/menu-items/` - Voir le contenu du panier
- `POST /api/cart/menu-items/` - Ajouter un article au panier
- `DELETE /api/cart/menu-items/` - Vider le panier

### Commandes
- `GET /api/orders/` - Lister les commandes (selon le rôle)
- `POST /api/orders/` - Créer une nouvelle commande à partir du panier
- `GET /api/orders/{id}/` - Détails d'une commande spécifique
- `PUT/PATCH /api/orders/{id}/` - Modifier une commande
- `DELETE /api/orders/{id}/` - Supprimer une commande (managers seulement)

## 🔑 Authentification

L'API utilise l'authentification par token. Pour obtenir un token :

```bash
POST /auth/token/login/
Content-Type: application/json

{
    "username": "your_username",
    "password": "your_password"
}
```

Puis utilisez le token dans l'en-tête Authorization :
```
Authorization: Token your_token_here
```

## 🎯 Fonctionnalités

### ✅ Fonctionnalités Implémentées

1. **Gestion des Utilisateurs**
   - L'admin peut assigner des utilisateurs au groupe manager
   - Accès au groupe manager avec token admin
   - Les managers peuvent se connecter
   - Les clients peuvent s'enregistrer et se connecter

2. **Gestion du Menu**
   - L'admin peut ajouter des articles de menu
   - L'admin peut ajouter des catégories
   - Les clients peuvent parcourir toutes les catégories
   - Les clients peuvent parcourir tous les articles de menu
   - Les clients peuvent parcourir les articles par catégorie
   - Pagination des articles de menu
   - Tri des articles par prix
   - Recherche et filtrage

3. **Gestion des Équipes**
   - Les managers peuvent assigner des utilisateurs à l'équipe de livraison
   - Les managers peuvent assigner des commandes à l'équipe de livraison

4. **Système de Commandes**
   - L'équipe de livraison peut accéder aux commandes qui leur sont assignées
   - L'équipe de livraison peut marquer une commande comme livrée
   - Les clients peuvent ajouter des articles au panier
   - Les clients peuvent accéder aux articles précédemment ajoutés au panier
   - Les clients peuvent passer des commandes
   - Les clients peuvent parcourir leurs propres commandes

5. **Fonctionnalités Avancées**
   - Permissions basées sur les rôles
   - Throttling pour les API
   - Pagination
   - Filtrage et tri
   - Recherche
   - Gestion d'erreurs appropriée

## 🗂️ Structure du Projet

```
LittleLemon/
├── LittleLemon/          # Configuration du projet Django
│   ├── settings.py       # Paramètres Django
│   ├── urls.py          # URLs principales
│   └── ...
├── LittleLemonAPI/       # Application principale
│   ├── models.py        # Modèles de données
│   ├── serializers.py   # Serializers DRF
│   ├── views.py         # Vues API
│   ├── urls.py          # URLs de l'API
│   ├── permissions.py   # Permissions personnalisées
│   ├── admin.py         # Configuration admin Django
│   └── management/      # Commandes de gestion personnalisées
├── db.sqlite3           # Base de données SQLite
├── manage.py            # Script de gestion Django
├── Pipfile              # Dépendances pipenv
└── notes.txt            # Notes et informations d'accès
```

## 🧪 Tests

Pour tester l'API, vous pouvez utiliser :
- **Navigateur** : http://127.0.0.1:8000/api/menu-items/
- **Panel Admin Django** : http://127.0.0.1:8000/admin/
- **Outils comme Insomnia ou Postman** pour tester les endpoints

## 📝 Notes Importantes

- La base de données SQLite est incluse dans le projet avec des données de test
- Tous les utilisateurs de test ont été créés
- Les groupes Manager et Delivery crew sont configurés
- L'API respecte toutes les exigences du projet Little Lemon
