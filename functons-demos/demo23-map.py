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


def set_price(product):
    product['price'] = product['price'] + product['price']*0.10
    return product


#set_price1= lambda product:product['price'] = product['price'] + product['price']*0.10 product

print(list(map(lambda p:p['price'] + p['price'] * 0.10, products)))


#print(list(map(set_price1, products)))
print(list(map(set_price, products)))
