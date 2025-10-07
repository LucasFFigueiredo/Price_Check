from concurrent.futures import ProcessPoolExecutor, as_completed

def _to_money(x):
    return round(float(x), 2)

def process_batch(products, productPrices, sales_by_product, tolerance):
    errors = 0
    catalog = {p: _to_money(pr) for p, pr in zip(products, productPrices)}
    for p, correct_price in catalog.items():
        for sold in sales_by_product.get(p, []):

            diff = abs(sold - correct_price)
            if diff > tolerance + 1e-9:
                errors += 1
    return errors

def chunked(seq, size):
    for i in range(0, len(seq), size):
        yield seq[i:i+size]

def price_check_parallel(products, productPrices, productSold, soldPrice,
                         batch_size=25, tolerance=0.01):

    sales_by_product = {}
    for prod, price in zip(productSold, soldPrice):
        sales_by_product.setdefault(prod, []).append(_to_money(price))

    total_errors = 0
    batches = list(zip(chunked(products, batch_size), chunked(productPrices, batch_size)))

    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = [
            executor.submit(process_batch, prod_batch, price_batch,
                            sales_by_product, tolerance)
            for prod_batch, price_batch in batches
        ]
        for f in as_completed(futures):
            total_errors += f.result()

    return total_errors


if __name__ == "__main__":

    products = [
        'bread', 'milk', 'cheese', 'butter', 'coffee', 'tea', 'rice', 'pasta',
        'apple', 'banana', 'chicken', 'fish', 'beef', 'orange', 'grape', 'cereal',
        'sugar', 'flour', 'yogurt', 'oil', 'water', 'juice', 'cookies', 'chips',
        'tomato', 'onion', 'lettuce', 'potato', 'salt', 'pepper', 'honey',
        'jam', 'soda', 'chocolate', 'icecream', 'beans', 'breadsticks', 'mushroom',
        'carrot', 'chewinggum'
    ]

    productPrices = [
        3.49, 2.99, 6.59, 5.49, 8.90, 4.50, 3.10, 2.79,
        1.99, 1.50, 12.99, 15.75, 17.49, 3.39, 4.20, 6.99,
        3.49, 4.99, 5.75, 7.89, 1.20, 6.00, 4.40, 5.50,
        2.70, 2.30, 1.80, 3.00, 1.10, 2.00, 8.90,
        5.10, 4.59, 9.80, 14.20, 6.60, 3.00, 7.40,
        2.25, 1.50
    ]

    productSold = [
        'milk', 'bread', 'coffee', 'banana', 'fish', 'cheese', 'milk', 'orange',
        'pasta', 'butter', 'rice', 'oil', 'sugar', 'cereal', 'bread', 'apple',
        'chicken', 'flour', 'grape', 'beef', 'juice', 'cookies', 'chips', 'pepper',
        'tea', 'coffee', 'salt', 'onion', 'honey', 'soda', 'chocolate', 'breadsticks',
        'icecream', 'beans', 'tomato', 'yogurt', 'rice', 'fish', 'mushroom', 'carrot'
    ]

    soldPrice = [
        3.00, 3.49, 8.95, 1.50, 15.76, 6.60, 2.98, 3.40, 2.75, 5.50,
        3.10, 7.91, 3.47, 6.98, 3.48, 2.00, 13.00, 5.02, 4.19, 17.50, 6.00,
        4.42, 5.51, 2.03, 4.50, 8.91, 1.12, 2.30, 8.88, 4.59, 9.82,
        3.00, 9.81, 6.61, 2.70, 5.76, 3.09, 15.77, 7.38, 2.26,
    ]

    result = price_check_parallel(products, productPrices, productSold, soldPrice)
    print(f"Number of pricing errors detected: {result}")
