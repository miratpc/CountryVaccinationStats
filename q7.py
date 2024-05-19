import pandas as pd
import numpy as np

# Read the dataset
df = pd.read_csv(r'C:\Users\TULPAR\Documents\GitHub\CountryVaccinationStats\country_vaccination_stats.csv')

# Impute missing values in 'daily vaccinations' with the minimum value of the respective country.
# If a country has all NaN values, it will fill with 0.
df['daily_vaccinations'] = df.groupby('country')['daily_vaccinations'].transform(lambda x: x.fillna(x.min() if not np.isnan(x.min()) else 0))

# Filter the dataset for the date 1/6/2021
df_filtered = df[df['date'] == '1/6/2021']

# Calculate the total vaccinations for the filtered date
total_vaccinations = df_filtered['daily_vaccinations'].sum()

# Display the result
print(total_vaccinations)
