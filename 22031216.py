import pandas as pd
import matplotlib.pyplot as plt


# Set file path
file_path = r'E:\Ahmed\Data.csv'

# Read file with header as the first row
data = pd.read_csv(file_path, header=0)

# Transpose the data to switch rows and columns
transposed_data = data.T

# Get the year columns
year_columns = transposed_data.iloc[3:]

# Clean the year columns by removing any non-numeric characters
year_columns = year_columns.apply(lambda x: pd.to_numeric(x.astype(str).str.replace(',', ''), errors='coerce'))

# Get the country columns
country_columns = transposed_data.iloc[:3].T

# Set the first three rows as the column headers
country_columns.columns = country_columns.iloc[0]

# Remove the first row since it is now a header row
country_columns = country_columns[1:]
# Filter year columns to only show data from years 2004 to 2014
year_columns = year_columns.loc['2004':'2014']



# Display the resulting dataframes
print("Year Columns:")
print(year_columns)
print("\nCountry Columns:")
print(country_columns)


selected_countries = country_columns.loc[country_columns['Country Name'].isin(['Aruba', 'Afghanistan', 'Angola', 'India'])]

# Drop the 'Country Code' and 'Indicator Name' columns
selected_countries = selected_countries.drop(['Country Code', 'Indicator Name'], axis=1)

# Calculate the mean for each row (i.e., each year) using the .mean() method
mean_by_year = selected_countries.mean(axis=0)

# Print the resulting mean values
print(mean_by_year)


# Create a dictionary with the data
data = {'Year': [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014],
        'Zambia': [2.5, 2.6, 2.7, 2.9, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2],
        'Afghanistan': [1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0],
        'Angola': [3.0, 3.1, 3.3, 3.5, 3.7, 3.9, 4.1, 4.3, 4.5, 4.7, 4.9],
        'India': [6.0, 6.2, 6.4, 6.6, 6.8, 7.0, 7.2, 7.4, 7.6, 7.8, 8.0]}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Set the 'Year' column as the index
df = df.set_index('Year')

# Calculate the mean for each row (i.e., each year) using the .mean() method
df['mean'] = df.mean(axis=1)



# Create a histogram with the mean values for each country
df['mean'].plot(kind='bar')
plt.xlabel('Country')
plt.ylabel('Mean Value')
plt.title('Mean Value of Selected Countries (2004-2014)')
plt.show()



# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Set the 'Year' column as the index
df = df.set_index('Year')

# Calculate the median for each country
median_values = df.median()

# Calculate the mode for each country
mode_values = df.mode().iloc[0]

# Calculate the skewness for each country
skewness_values = df.skew()



# Plot a bar chart of median and mode values for each country
fig, ax = plt.subplots()
ax.bar(median_values.index, median_values.values, label='Median', color='blue', alpha=0.5)
ax.bar(mode_values.index, mode_values.values, label='Mode', color='red', alpha=0.5)
ax.set_title('Median and Mode Values')
ax.set_xlabel('Country')
ax.set_ylabel('Value')
ax.legend()
plt.show()



# Plot a line chart of skewness values over time for each country
fig, ax = plt.subplots()
ax.plot(skewness_values.index, skewness_values.values, label='Skewness', color='green')
ax.set_title('Skewness Values over Time')
ax.set_xlabel('Year')
ax.set_ylabel('Skewness')
ax.legend()
plt.show()
