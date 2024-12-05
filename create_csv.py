import pandas as pd

# 1. Sales Data
sales_data = {
    'transaction_id': [1, 2, 3, 4, 5],
    'date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-02-01', '2024-02-05'],
    'product_id': [101, 102, 103, 101, 104],
    'quantity': [2, 3, 1, 4, 5],
    'revenue': [200, 300, 150, 400, 500]
}

sales_df = pd.DataFrame(sales_data)
sales_df.to_csv('database/sales_data.csv', index=False)

# 2. Category Share Data
category_share_data = {
    'date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-02-01', '2024-02-05'],
    'product_id': [101, 102, 103, 104, 101],
    'market_share': [20, 15, 10, 25, 30]
}

category_share_df = pd.DataFrame(category_share_data)
category_share_df.to_csv('database/category_share_data.csv', index=False)

product_category_mapping = {
    'product_id': [101, 102, 103, 104],
    'category_id': ['A', 'B', 'A', 'C']
}

product_category_mapping_df = pd.DataFrame(product_category_mapping)
product_category_mapping_df.to_csv('database/product_category_mapping.csv', index=False)

print("CSV files created successfully.")
