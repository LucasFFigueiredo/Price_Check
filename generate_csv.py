import random

def generate_catalog(path="catalog.csv", n_products=1000):
    """Gera um catálogo com n_products produtos e preços base."""
    with open(path, "w", encoding="utf-8") as f:
        for i in range(1, n_products + 1):
            name = f"product_{i:04}"
            price = round(random.uniform(1.00, 100.00), 2)
            f.write(f"{name},{price}\n")
    print(f"✅ Gerado {path} com {n_products} produtos.")


def generate_sales(path="sales.csv", catalog_path="catalog.csv", n_sales=1_000_000):
    """Gera um arquivo de vendas simuladas com base no catálogo."""
    with open(catalog_path, "r", encoding="utf-8") as f:
        catalog = [line.strip().split(",") for line in f if line.strip()]

    with open(path, "w", encoding="utf-8") as f:
        for _ in range(n_sales):
            product, price_str = random.choice(catalog)
            price = float(price_str)

            if random.random() < 0.8:
                delta = random.choice([-0.01, 0.00, 0.01])
            else:
                delta = round(random.uniform(-0.10, 0.15), 2)

            sold_price = round(price + delta, 2)
            f.write(f"{product},{sold_price}\n")

    print(f"✅ Gerado {path} com {n_sales:,} vendas simuladas.")


if __name__ == "__main__":
    generate_catalog("catalog.csv", n_products=1000)
    generate_sales("sales.csv", catalog_path="catalog.csv", n_sales=1_000_000)
    print("🏁 Dados prontos! Agora rode: python price_check_stream_chunked.py")
