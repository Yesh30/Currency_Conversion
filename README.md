# PythonCodes

To accomplish this task, you can use Python to fetch the currency conversion rates against the US Dollar from an API, and then save the data into an Excel file. Here's a step-by-step script for that:

### Necessary Libraries
1. `requests` for fetching data from the API.
2. `json` for handling JSON data.
3. `pandas` for data manipulation and saving to Excel.
4. `openpyxl` as an Excel engine for pandas (optional, but recommended).

You can install the necessary libraries using:
```bash
pip install requests pandas openpyxl
```

### Step-by-Step Script

1. **Set up the script:**
2. **Fetch data:**
3. **Manipulate and save data to Excel:**

Here is the complete script:

```python
import requests
import json
import pandas as pd
from datetime import datetime

# Replace 'YOUR_ACCESS_KEY' with your actual API key from fixer.io
api_key = 'YOUR_ACCESS_KEY'
url = f"http://data.fixer.io/api/latest?access_key={api_key}"

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
```

### Explanation

1. **Setup:**
   - Import necessary libraries.
   - Provide your API key from Fixer.io.
   - Define the URL for fetching the latest exchange rates.

2. **Fetch Data from API:**
   - Use the `requests` library to fetch data from the API.
   - Convert the JSON response to a Python dictionary.

3. **Manipulate Data:**
   - Check if the API request was successful.
   - Extract the exchange rates.
   - Calculate the conversion rate of each currency against the USD.
   - Create a pandas DataFrame from the conversion rates.
   - Add a timestamp column for when the data was fetched.

4. **Save Data to Excel:**
   - Use pandas to save the DataFrame to an Excel file.

### Running the Script

Save the script in a Python file (e.g., `currency_to_excel.py`), run it, and it will create an Excel file (`currency_rates.xlsx`) in the same directory with the latest conversion rates against the USD.

```bash
python currency_to_excel.py
```

This approach ensures you have the most up-to-date currency conversion rates stored in an easily accessible and editable format.
