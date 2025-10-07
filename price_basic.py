def priceCheck(products, productPrices, productSold, soldPrice):
    erros = 0
    for i in range(len(productSold)):
        product = productSold[i]
        sold = soldPrice[i]
        correct_price = productPrices[products.index(product)]
        
        diff = abs(sold - correct_price)
        
        if diff > 0.01:
            erros += 1
    return erros



products = [
    'bread', 'milk', 'cheese', 'butter', 'coffee',
    'tea', 'rice', 'pasta', 'apple', 'banana',
    'chicken', 'fish', 'beef', 'orange', 'grape',
    'cereal', 'sugar', 'flour', 'yogurt', 'oil'
]

productPrices = [
    3.49, 2.99, 6.59, 5.49, 8.90,
    4.50, 3.10, 2.79, 1.99, 1.50,
    12.99, 15.75, 17.49, 3.39, 4.20,
    6.99, 3.49, 4.99, 5.75, 7.89
]

productSold = [
    'milk', 'bread', 'coffee', 'banana', 'fish', 'cheese',
    'milk', 'orange', 'pasta', 'butter', 'rice', 'oil',
    'sugar', 'cereal', 'bread', 'apple', 'chicken', 'flour',
    'grape', 'beef'
]

soldPrice = [
    3.00, 3.49, 8.95, 1.50, 15.75, 6.60, 2.98, 3.40, 
    2.75, 5.50, 3.10, 7.90, 3.47, 6.98, 3.48, 2.00,
    13.00, 5.02, 4.19, 17.50 
]


result = priceCheck(products, productPrices, productSold, soldPrice)

print(f"Number of pricing errors detected: {result}")