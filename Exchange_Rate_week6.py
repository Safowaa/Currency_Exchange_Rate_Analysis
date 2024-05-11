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


# What is the distribution of exchange rates for the Chinese Yuan (CNY) against the Euro (EUR)?
# visualize it.
# Plotting a histogram of the exchange rates for CNY

sns.histplot(data=frank2, x="CNY", kde=True, edgecolor='black', color = "green")
plt.xlabel("Exchange Rate(CNY)")  
plt.ylabel("Frequency")                 
plt.title("Distribution Of The Exchange Rates For CNY")

# Displaying the plot
plt.show

# This code segment creates a histogram to visualize the distribution
# of exchange rates for CNY (Chinese Yuan). The data is retrieved from the DataFrame 
# frank2, with the exchange rates represented by the column 'CNY'. The histogram is customized
# with KDE (Kernel Density Estimation) enabled, edge color set to black, and histogram bars 
# colored green. Axis labels and a title are added for clarity, and the plot is displayed using plt.show().

# 3. Between the Great British Pound (GBP) and the Japanese Yen (JPY) determine which country's currency is more volatile
# A Bar chart comparing the volatility of the selected currencies.


# Calculate volatility (standard deviation) for GBP to JPY exchange rate & vice-versa
volt_gbp_jpy = frank2['GBP'].std()
volt_jpy_gbp = frank2['JPY'].std()

# Creating a bar plot to compare volatility
sns.barplot(x=['GBP to JPY', 'JPY to GBP'], y=[volt_gbp_jpy, volt_jpy_gbp])
plt.xlabel("Exchange Rates")                                                             
plt.ylabel("Volatility")                                          
plt.title("More Volatile Currency")  

# Adding labels to the bars
for i in range(len(['GBP to JPY', 'JPY to GBP'])):
    plt.text(i, [volt_gbp_jpy, volt_jpy_gbp][i], f'{[volt_gbp_jpy, volt_jpy_gbp][i]:.2f}', ha='center', va='bottom')
    
# Displaying the plot
plt.show()

# This code creates a bar plot using seaborn to compare the volatility
# (standard deviation) between GBP to JPY and JPY to GBP exchange rates from 
# the DataFrame frank2. Axis labels and a title are added for clarity.
# Additionally, labels are added to the bars to display the volatility values. The plot is displayed using plt.show().

# 4. Is there a correlation between the exchange rates of the Canadian Dollar (CAD) and the American Dollar (USD) ??
# Visualize using a Scatter plot.
# Calculating the correlation coefficient between CAD and USD
cor_coefficient = frank2['CAD'].corr(frank2['USD'])

# Creating a scatter plot to visualize the relationship between CAD and USD
sns.scatterplot(data=frank2, x="CAD", y="USD", alpha=0.6)  # Scatter plot with transparency set to 0.6

# Adding kernel density estimation (KDE) to the plot
sns.kdeplot(data=frank2, x="CAD", y="USD", color="green", levels=5, linewidths=1)  # KDE plot with green color, 5 contour levels, and linewidth of 1

# Adding labels and title to the plot
plt.xlabel("CAD") 
plt.ylabel("USD")    
plt.title("Correlation between CAD and USD")  # Title

# Displaying the plot
plt.show()

# This code segment calculates the correlation coefficient between the Canadian Dollar (CAD) and the US Dollar (USD)
# exchange rates from the DataFrame frank2. It then creates a scatter plot to visualize the relationship between CAD
# and USD exchange rates, with transparency set to 0.6. Additionally, kernel density estimation (KDE) is added to the
# plot to show the density of points. Axis labels and a title are included for clarity, and the plot is displayed using plt.show().
