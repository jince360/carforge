from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.utils import timezone
# Create your models here.

STATE_CHOICES = [
    ("AP", "Andhra Pradesh"),
    ("AR", "Arunachal Pradesh"),
    ("AS", "Assam"),
    ("BR", "Bihar"),
    ("CT", "Chhattisgarh"),
    ("GA", "Goa"),
    ("GJ", "Gujarat"),
    ("HR", "Haryana"),
    ("HP", "Himachal Pradesh"),
    ("JH", "Jharkhand"),
    ("KA", "Karnataka"),
    ("KL", "Kerala"),
    ("MP", "Madhya Pradesh"),
    ("MH", "Maharashtra"),
    ("MN", "Manipur"),
    ("ML", "Meghalaya"),
    ("MZ", "Mizoram"),
    ("NL", "Nagaland"),
    ("OR", "Odisha"),
    ("PB", "Punjab"),
    ("RJ", "Rajasthan"),
    ("SK", "Sikkim"),
    ("TN", "Tamil Nadu"),
    ("TG", "Telangana"),
    ("TR", "Tripura"),
    ("UP", "Uttar Pradesh"),
    ("UK", "Uttarakhand"),
    ("WB", "West Bengal"),
]


class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)
    logo = models.ImageField(upload_to="brand_logos/", blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True, db_index=True)
    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class CarType(models.Model):
    CAR_TYPE_CHOICES = [
        ("sedan", "Sedan"),
        ("coupe", "Coupe"),
        ("convertible", "Convertible"),
        ("suv", "SUV"),
        ("crossover", "Crossover"),
        ("limousine", "Limousine"),
        ("sports", "Sports Car"),
        ("supercar", "Super Car"),
        ("gt", "Grand Tourer"),
    ]

    car_type = models.CharField(max_length=20, choices=CAR_TYPE_CHOICES)

    class Meta:
        verbose_name = "Car Type"
        verbose_name_plural = "Car Types"

    def __str__(self):
        return self.get_car_type_display()

class FuelType(models.Model):
    FUEL_CHOICE = [
        ("pet", "Petrol"),
        ("des", "Diesel"),
        ("ele", "Electric"),
        ("hyd", "Hybrid"),
    ]

    fuel = models.CharField(choices=FUEL_CHOICE, max_length=10, unique=True)

    class Meta:
        verbose_name = "Fuel Type"
        verbose_name_plural = "Fuel Types"
    
    def __str__(self):
        return self.get_fuel_display()
    
class Condition(models.Model):
    CONDITION_CHOICE = [
    ("excellent", "Excellent"),
    ("very_good", "Very Good"),
    ("good", "Good"),
    ("fair", "Fair"),
    ("poor", "Poor"),
    ]

    condition = models.CharField(choices=CONDITION_CHOICE, max_length=20, unique=True)

    class Meta:
        verbose_name = "Condition"
        verbose_name_plural = "Conditions"

    def __str__(self):
        return self.get_condition_display()
    
class Feature(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta:
        verbose_name = "Feature"
        verbose_name_plural = "Features"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Transmission(models.Model):
    TRANSMISSION_CHOICE = [
        ("manual", "Manual"),
        ("automatic", "Automatic"),
    ]
    transmission = models.CharField(max_length=50, choices=TRANSMISSION_CHOICE)

    class Meta:
        verbose_name = "Transmission"
        verbose_name_plural = "Transmissions"
    
    def __str__(self):
        return self.get_transmission_display()
    

class Color(models.Model):

    name = models.CharField(max_length=50, unique=True)
    hexcode = models.CharField(max_length=7, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True)

    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name



def validate_year(value):
    current_year = timezone.now().year
    if value < 1975 or value > current_year:
        raise ValidationError(f"Year must be between 1975 and {current_year}")

def validate_vin(value):
    if len(value) != 17 or not value.isalnum():
        raise ValidationError("VIN must be exactly 17 alphanumeric characters")
   
class Car(models.Model):
    DOOR_CHOICE = [
        (str(i), str(i)) for i in range(2, 7)
    ]

    SEAT_CHOICE =[
        (str(i), str(i)) for i in range(2, 9)] + [("oth", "Others")
    ]
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, related_name="car_brand")
    model = models.CharField(max_length=50)
    type =  models.ForeignKey(CarType, on_delete=models.CASCADE, related_name="cars")
    year = models.PositiveIntegerField(validators=[validate_year])
    door_type = models.CharField(choices=DOOR_CHOICE, max_length=2)
    color = models.ForeignKey(Color,on_delete=models.SET_NULL, null=True)
    condition = models.ForeignKey(Condition, on_delete=models.SET_NULL, null=True, related_name="car_condition")
    price = models.DecimalField(max_digits=12, decimal_places=2)
    state = models.CharField(choices=STATE_CHOICES, max_length=2)
    description = models.TextField(blank=True)
    featured_image = models.ImageField(upload_to="car_images")
    car_features = models.ManyToManyField(Feature, related_name="car_features")
    fuel = models.ForeignKey(FuelType, on_delete=models.SET_NULL, null=True)
    transmission = models.ForeignKey(Transmission, on_delete=models.SET_NULL, null=True)
    mileage_km = models.PositiveIntegerField()
    seating_capacity = models.CharField(choices=SEAT_CHOICE, max_length=10)
    identification_number = models.CharField(max_length=17, unique=True, validators=[validate_vin])
    number_of_owners = models.PositiveIntegerField()
    is_featured = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"
    
    def __str__(self):
        return f"{self.brand.name} - {self.model} - {self.identification_number}"

class AdditionalImages(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="car_images")
    image = models.ImageField(upload_to="car_images")

    class Meta:
        verbose_name = "Additional image"
        verbose_name_plural = "Additional images"

    def __str__(self):
        return f"{self.car.brand.name} - images"