from django.contrib import admin

# Register your models here.
from .models import Category, IceCream, Topping, Wrapper

admin.site.register([Category, IceCream, Topping, Wrapper])