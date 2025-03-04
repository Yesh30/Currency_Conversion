import requests
import json
import pandas as pd
from datetime import datetime

# Replace 'YOUR_ACCESS_KEY' with your actual API key from fixer.io
api_key = 'ebd6a1e4d2c791c78cf00e4be16d4439'
url = f"http://data.fixer.io/api/latest?access_key=ebd6a1e4d2c791c78cf00e4be16d4439"

# Fetching the data
response = requests.get(url)
data = response.json()

# Checking if the request was successful
if data['success']:
    # Get the currency rates
    rates = data['rates']

    # USD to other currencies
    usd_to_others = {currency: rate / rates['USD'] for currency, rate in rates.items()}

    # Creating a DataFrame
    df = pd.DataFrame(list(usd_to_others.items()), columns=['Currency', 'Rate'])
    
    # Adding a timestamp
    df['Timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Saving to Excel
    excel_file = 'currency_rates.xlsx'
    df.to_excel(excel_file, index=False)
    
    print(f"Currency conversion rates against USD have been saved to {excel_file}")
else:
    print("Failed to retrieve data:", data['error']['info'])
