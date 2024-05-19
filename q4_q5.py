import pandas as pd

# Read the dataset
df = pd.read_csv(r'C:\Users\TULPAR\Documents\GitHub\CountryVaccinationStats\country_vaccination_stats.csv')


# Group by country and find the minimum daily vaccinations for each country
min_daily_vaccinations = df.groupby('country')['daily_vaccinations'].min().reset_index()

# Create a dictionary to map countries to their minimum daily vaccinations
min_vaccinations_dict = dict(zip(min_daily_vaccinations['country'], min_daily_vaccinations['daily_vaccinations']))

# Function to impute missing data
def impute_missing(row):
    country = row['country']
    daily_vaccinations = row['daily_vaccinations']
    if pd.isnull(daily_vaccinations):  # If daily vaccinations is missing
        if country in min_vaccinations_dict:  # If country has valid data
            return min_vaccinations_dict[country]
        else:
            return 0  # If country has no valid data
    else:
        return daily_vaccinations

# Apply the imputation function
df['daily_vaccinations'] = df.apply(impute_missing, axis=1)

# Output the dataframe with imputed values
print(df)

# Write the updated dataframe to a new CSV file
df.to_csv('imputed_vaccination_data.csv', index=False)