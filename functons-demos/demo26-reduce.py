from functools import reduce

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
product_prices = map(lambda product: product['price'], products)

sum_all = reduce(lambda x1, x2: x1 + x2, product_prices)
print("sum of all product prices = ", sum_all)

sum_all = reduce(lambda a, b: a + b, map(lambda product: product['price'], products))
print("sum of all product prices = ", sum_all)
