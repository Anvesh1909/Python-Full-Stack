import random
from products.models import Category, Product  # replace `myapp` with your actual app name

# Sample categories
category_names = ['Beverages', 'Snacks', 'Dairy', 'Bakery', 'Frozen Foods']
categories = {}

# Create or get categories
for name in category_names:
    category, _ = Category.objects.get_or_create(name=name)
    categories[name] = category

# Sample data for generation
brands = ['Nestle', 'PepsiCo', 'Amul', 'Britannia', 'Coca-Cola', 'Parle']
product_names = [
    'Milk Packet', 'Cheese Slice', 'Bread Loaf', 'Butter', 'Yogurt',
    'Apple Juice', 'Orange Soda', 'Potato Chips', 'Chocolate Bar',
    'Frozen Peas', 'Frozen French Fries', 'Muffins', 'Cookies',
    'Ice Cream', 'Cold Coffee', 'Green Tea', 'Energy Drink',
    'Wheat Flour', 'Basmati Rice', 'Instant Noodles'
]

# Generate 20 products
for i in range(20):
    name = product_names[i]
    category = random.choice(list(categories.values()))
    brand = random.choice(brands)
    price = round(random.uniform(10, 200), 2)
    stock = random.randint(10, 100)
    
    Product.objects.create(
        name=name,
        category=category,
        brand=brand,
        price=price,
        stock=stock,
        is_available=True,
        description=f"{name} by {brand} in {category.name} category."
    )

print("✅ 20 products created successfully!")
