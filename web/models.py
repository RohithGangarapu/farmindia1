from django.db import models

# Producer and Customer will share the same structure
class Producer(models.Model):
    name = models.CharField(max_length=100)
    # photo = models.ImageField(upload_to='photos/')
    password = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    # coordinates = models.JSONField()  # Store x, y as {"x": value, "y": value}
    phone_no = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name
class Consumer(models.Model):
    name = models.CharField(max_length=100)
    # photo = models.ImageField(upload_to='photos/')
    password = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    # coordinates = models.JSONField()  # Store x, y as {"x": value, "y": value}
    phone_no = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')
    type = models.CharField(max_length=100)
    desc=models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Consumption(models.Model):
    product = models.ManyToManyField(Product, related_name="consumptions")
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE, related_name="consumptions")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Consumption by {self.customer.name} - Total Price: {self.price}"

class Transition(models.Model):
    onsumer = models.ForeignKey(Consumer, on_delete=models.CASCADE, related_name="transitions")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="transitions")
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, related_name="produced_transitions")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Transition: {self.product.name} - {self.customer.name} to {self.producer.name}"

class PastPrices(models.Model):
    product = models.CharField(max_length=100)
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Past Price of {self.product} on {self.date} - {self.price}"
