products = [
    {
        'product_id': 101,
        'product_name': 'laptop',
        'price': 100,
        'category': 'electronics',
        'is_available': True
    },
    {
        'product_id': 11,
        'product_name': 'mobile',
        'price': 49000,
        'category': 'electronics',
        'is_available': False
    },
    {
        'product_id': 78,
        'product_name': 'headphone',
        'price': 899,
        'category': 'electronics',
        'is_available': True
    },
    {
        'product_id': 78,
        'product_name': 'camera',
        'price': 99,
        'category': 'electronics',
        'is_available': True
    },
    {
        'product_id': 73,
        'product_name': 'shirt',
        'price': 3700,
        'category': 'clothes',
        'is_available': True
    }
]

for product in products:
    if product['category'] != 'electronics':
        print(product)

print("using lambda function")
print(list(filter(lambda p : p['category'] !='electronics',products )))