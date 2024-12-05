from flask import Flask, request, jsonify,render_template
import pandas as pd

app = Flask(__name__)

sales_data = pd.read_csv('database/sales_data.csv')
category_share_data = pd.read_csv('database/category_share_data.csv')
product_category_mapping = pd.read_csv('database/product_category_mapping.csv')

sales_data = sales_data.merge(product_category_mapping, on='product_id', how='left')
print(sales_data)
@app.route('/')
def home():
        return render_template("index.html")

@app.route('/total_sales', methods=['GET'])
def total_sales():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')


    filtered_data = sales_data[(sales_data['date'] >= start_date) & (sales_data['date'] <= end_date)]
    total_sales = filtered_data['revenue'].sum()

    return jsonify({'total_sales': int(total_sales)})


@app.route('/sales_by_category', methods=['GET'])
def sales_by_category():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    filtered_data = sales_data[(sales_data['date'] >= start_date) & (sales_data['date'] <= end_date)]
    sales_by_category = filtered_data.groupby('category_id')['revenue'].sum().reset_index()
    return sales_by_category.to_json(orient='records')

@app.route('/market_share_changes', methods=['GET'])
def market_share_changes():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    # Filter the category share data based on the date range
    filtered_data = category_share_data[(category_share_data['date'] >= start_date) & (category_share_data['date'] <= end_date)]

    # Merge with product-category mapping to get category IDs
    merged_data = filtered_data.merge(product_category_mapping, on='product_id', how='left')

    # Calculate the min and max market share for each category
    category_share_changes = merged_data.groupby('category_id')['market_share'].agg(['min', 'max']).reset_index()
    category_share_changes['share_change'] = category_share_changes['max'] - category_share_changes['min']

    # Sort the changes by the magnitude of the share change
    significant_changes = category_share_changes.sort_values(by='share_change', ascending=False)

    # Return the data as JSON
    return significant_changes.to_json(orient='records', default_handler=str)

