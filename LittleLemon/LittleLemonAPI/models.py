from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=255, db_index=True)  # Garder name pour la compatibilité
    title = models.CharField(max_length=255, db_index=True)  # Ajouter title comme dans la référence

    def __str__(self):
        return self.title or self.name

class MenuItem(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)  # PROTECT au lieu de CASCADE
    featured = models.BooleanField(db_index=True, default=False)

    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()  # SmallIntegerField pour la compatibilité
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('menuitem', 'user')  # Ordre comme dans la référence

    def __str__(self):
        return f"{self.user.username} - {self.menuitem.title} ({self.quantity})"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='delivery_crew', null=True)
    status = models.BooleanField(default=0, db_index=True)  # default=0 comme dans la référence
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0)  # max_digits=6 comme dans la référence
    date = models.DateField(db_index=True)  # DateField au lieu de DateTimeField

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('order', 'menuitem')

    def __str__(self):
        return f"{self.quantity} x {self.menuitem.title}"