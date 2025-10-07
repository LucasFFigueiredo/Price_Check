# 🧾 Price Check Project
A Python-based system that analyzes and detects price inconsistencies in sales transactions, comparing catalog prices with transaction records.
This project was developed progressively — from a simple comparison script to a scalable system capable of processing over 1 million sales efficiently.

---

## ✨ Features

- 📊 Detects price discrepancies between catalog and transaction values
- 💰 Accepts a tolerance margin of ± R$0.01 (to account for rounding or typing noise)
- ⚙️ Processes up to 1,000,000 sales efficiently, using chunk-based streaming

## 🧩 Includes:

- price_check_basic.py → basic comparison
- price_check_parallel.py → parallel (multi-core) processing
- price_check_stream_chunked.py → large-scale streaming version
- generate_large_csvs.py → creates test datasets (catalog.csv, sales.csv)

## 🧠 Why This Approach

The project demonstrates how to evolve a simple algorithm into a scalable data-processing solution:

- Stage	Script	Description
  - 🧮 Basic	price_check_basic.py	Simple and readable logic for small lists
  - ⚡ Parallel	price_check_parallel.py	Divides workload across CPU cores for speed
  - 🚀 Streaming	price_check_stream_chunked.py	Reads large datasets in chunks to handle millions of records
  - 🧰 Generator	generate_large_csvs.py	Creates realistic test data for validation

💡 Each version keeps the same core logic — counting products where the price difference exceeds R$0.01 — but optimizes how the data is read and processed.

##🧩 How to Run

1️⃣ Generate the dataset
Run the generator to create sample data for testing:
```
python generate_large_csvs.py
```
This creates:

catalog.csv → 1,000 products with base prices

sales.csv → 1,000,000 simulated sales (80% correct, 20% with errors)

2️⃣ Run the large-scale verifier
Execute the main script that reads in chunks:
```
python price_check_stream_chunked.py
```

Example output:
```
Erros detectados: 176142
```
🧮 About 17% of sales contain real discrepancies (> R$0.01), matching the data generation logic.

🧩 Adjustable Parameters

Inside price_check_stream_chunked.py:
```
CHUNK_SIZE = 250_000   # lines per batch (adjust for performance)
TOLERANCE  = 1         # 1 cent (0.01 R$)
```
## 🧠 Technical Notes

 - 🧾 Integer-based comparison: all prices are converted to centavos (e.g., 3.79 → 379) → eliminates floating-point errors.

 - 💡 Streaming I/O: only one chunk of sales stays in memory at a time. → makes it possible to process multi-gigabyte files.

 - 🧠 Algorithmic complexity: O(n) — each sale is checked exactly once.

 - 🔁 Scalable design: easily adaptable for MapReduce or multiprocessing extensions.

# ✍️ Author and motivation

This project was developed with an educational and technical focus, to demonstrate best practices for scalability, parallelism, and numerical tolerance in Python.

The evolution between the three versions shows the reasoning behind a system that starts simple and evolves as the volume of data increases.
