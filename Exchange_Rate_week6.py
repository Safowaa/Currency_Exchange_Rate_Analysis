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


#Normalize the rates column
frank_rates = pd.json_normalize(frank["rates"]) 
frank_rates

# Reset date as index instead
frank = frank.reset_index() 
frank.head()

# drop rate column
frank = frank.drop("rates", axis=1) 

# #concat dataframe with the normalised rate column
frank = pd.concat([frank, frank_rates], axis=1) 
frank.head()

# Create a new dataframe using only the rates required for the work
frank2 = frank[['index', 'amount', 'base', 'start_date', 'end_date','CAD', 'CNY', 'GBP', 'JPY', 'USD']].copy() 
        
         
frank2

# Convert all dates to datetime datatype
frank2["start_date"] = pd.to_datetime(frank2["start_date"]) 
frank2["end_date"] = pd.to_datetime(frank2["end_date"])
frank2["index"] = pd.to_datetime(frank2["index"])

#1. How has the exchange rate of the Euro (EUR) against the US Dollar (USD) changed over time?
#A line chart showing the exchange rate for EUR to USD


# Set the size of the plot
plt.figure(figsize=(10, 6))

# Plotting the exchange rate of EUR to USD
plt.plot(frank2['index'], frank2['USD'], linestyle='-') 

# Adding title and labels to the plot
plt.title('Exchange Rate of EUR to USD Over Time')
plt.xlabel('Year')               
plt.ylabel('Exchange Rate')     

# Turning off the grid lines
plt.grid(False)                    

# Displaying the plot
plt.show()  
# a line plot showing the exchange rate of EUR to USD over time. 
# The data for the plot is retrieved from the DataFrame frank2, 
# where 'index' represents the dates and 'USD' represents the corresponding 
# exchange rates. The plot is customized with a title and axis labels


