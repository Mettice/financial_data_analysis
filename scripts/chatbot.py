from flask import Flask, request, jsonify, send_from_directory
import pandas as pd

import os

# At the start of your script
print("Current working directory:", os.getcwd())
print("Attempting to load file from:", os.path.abspath('data/10k filings 2022-2024 fy_updated.csv'))

app = Flask(__name__)

# Load the financial data
df = pd.read_csv('data/10k filings 2022-2024 fy_updated.csv')

# Helper functions
def get_total_revenue_for_company(company):
    total_revenue = df[df['Company'] == company]['Total Revenue'].sum()
    return f"The total revenue for {company} is ${total_revenue:.2f} million."

def get_net_income_change_for_company(company):
    company_data = df[df['Company'] == company]
    net_income_change = company_data['Net Income'].iloc[-1] - company_data['Net Income'].iloc[0]
    return f"The net income for {company} has changed by ${net_income_change:.2f} million over the last year."

def get_revenue_growth_for_company(company):
    company_data = df[df['Company'] == company]
    growth = company_data['Revenue Growth (%)'].iloc[-1]
    return f"The revenue growth for {company} is {growth:.2f}%."

def get_net_income_growth_for_company(company):
    company_data = df[df['Company'] == company]
    growth = company_data['Net Income Growth (%)'].iloc[-1]
    return f"The net income growth for {company} is {growth:.2f}%."

def get_aggregate_statistics_for_company(company):
    company_data = df[df['Company'] == company]
    revenue_mean = company_data['Total Revenue'].mean()
    net_income_mean = company_data['Net Income'].mean()
    return (f"Average revenue for {company} is ${revenue_mean:.2f} million. "
            f"Average net income is ${net_income_mean:.2f} million.")

def simple_chatbot(user_query):
    user_query = user_query.lower()
    response = []

    if "microsoft" in user_query:
        if "revenue" in user_query:
            response.append(get_total_revenue_for_company("Microsoft"))
        elif "net income" in user_query:
            response.append(get_net_income_change_for_company("Microsoft"))
        elif "growth" in user_query:
            response.append(get_revenue_growth_for_company("Microsoft"))
            response.append(get_net_income_growth_for_company("Microsoft"))
        else:
            response.append(get_aggregate_statistics_for_company("Microsoft"))

    if "apple" in user_query:
        if "revenue" in user_query:
            response.append(get_total_revenue_for_company("Apple"))
        elif "net income" in user_query:
            response.append(get_net_income_change_for_company("Apple"))
        elif "growth" in user_query:
            response.append(get_revenue_growth_for_company("Apple"))
            response.append(get_net_income_growth_for_company("Apple"))
        else:
            response.append(get_aggregate_statistics_for_company("Apple"))

    if "tesla" in user_query:
        if "revenue" in user_query:
            response.append(get_total_revenue_for_company("Tesla"))
        elif "net income" in user_query:
            response.append(get_net_income_change_for_company("Tesla"))
        elif "growth" in user_query:
            response.append(get_revenue_growth_for_company("Tesla"))
            response.append(get_net_income_growth_for_company("Tesla"))
        else:
            response.append(get_aggregate_statistics_for_company("Tesla"))

    if response:
        return " ".join(response)
    else:
        return "Sorry, I can only provide information on Microsoft, Apple, or Tesla."

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        data = request.get_json()
        user_query = data.get('query', '')
    else:
        user_query = request.args.get('query', '')

    response = simple_chatbot(user_query)
    return jsonify({'response': response})

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

if __name__ == "__main__":
    app.run(debug=True)