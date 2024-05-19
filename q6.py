import pandas as pd
import numpy as np

# Read the dataset
df = pd.read_csv(r'C:\Users\TULPAR\Documents\GitHub\CountryVaccinationStats\country_vaccination_stats.csv')

# Impute missing values in 'daily vaccinations' with the minimum value of the respective country.
# If a country has all NaN values, it will fill with 0.
df['daily_vaccinations'] = df.groupby('country')['daily_vaccinations'].transform(lambda x: x.fillna(x.min() if not np.isnan(x.min()) else 0))

# Calculate the median of daily vaccinations for each country
median_vaccinations = df.groupby('country')['daily_vaccinations'].median().reset_index()

# Sort the countries by median daily vaccinations in descending order
median_vaccinations_sorted = median_vaccinations.sort_values(by='daily_vaccinations', ascending=False)

# Get the top 3 countries
top_3_countries = median_vaccinations_sorted.head(3)

# Display the results
print(top_3_countries)
