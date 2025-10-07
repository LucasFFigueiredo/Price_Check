def to_cents(value):
    value = str(value).replace(',', '.').strip()
    return int(round(float(value) * 100))

def load_catalog(path):
    catalog = {}
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            if len(parts) < 2:
                continue
            prod = parts[0].strip()
            price_cents = to_cents(parts[1])
            catalog[prod] = price_cents
    return catalog

def process_chunk(lines, catalog, tolerance_cents):
    errors = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split(',')
        if len(parts) < 2:
            continue
        prod = parts[0].strip()
        if prod not in catalog:

            continue
        sold_cents = to_cents(parts[1])
        if abs(sold_cents - catalog[prod]) > tolerance_cents:
            errors += 1
    return errors

def count_price_errors_chunked(catalog, sales_path, tolerance_cents=1, chunk_size=250_000):
    total_errors = 0
    buffer = []
    with open(sales_path, 'r', encoding='utf-8') as f:
        for line in f:
            buffer.append(line)
            if len(buffer) >= chunk_size:
                total_errors += process_chunk(buffer, catalog, tolerance_cents)
                buffer = []

        if buffer:
            total_errors += process_chunk(buffer, catalog, tolerance_cents)
    return total_errors

if __name__ == "__main__":

    CHUNK_SIZE = 250_000
    TOLERANCE  = 1

    catalog = load_catalog("catalog.csv")
    total = count_price_errors_chunked(catalog, "sales.csv",
                                       tolerance_cents=TOLERANCE,
                                       chunk_size=CHUNK_SIZE)
    print("Erros detectados:", total)