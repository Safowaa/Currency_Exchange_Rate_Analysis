import pandas as pd
import requests 
import matplotlib.pyplot as plt
import sqlalchemy 
from pandas import json_normalize
import seaborn as sns
import numpy as np 


# Define the start date and end date of the desired date range according to the question asked
"2013-01-01..2023-12-31"
# Construct the URL with the start date and end date
url = "https://api.frankfurter.app/2013-01-01..2023-12-31"

# Make a GET request to the API
response = requests.get(url)

# Turn it into a json
data = response.json()
data


# Changing to a dataframe
frank = pd.DataFrame(data)
frank.head()



