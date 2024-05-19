import re
import pandas as pd


data = {
    'Device_Type': ['AXO145', 'BXO234', 'CYO567'],
    'Stats_Access_Link': [
        '<url>https://xcd32112.smart_meter.com/data</url>',
        '<url>http://abc123_4.electric_meter.net/info</url>',
        '<url>https://xyz7890.smart_meter.org/details</url>'
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define the regular expression to extract the URL
url_pattern = re.compile(r'<url>https?://([a-zA-Z0-9_.]+)</url>')

# Function to extract pure URL
def extract_url(access_link):
    match = url_pattern.search(access_link)
    if match:
        return match.group(1)
    return None

# Apply the function to the Stats_Access_Link column
df['Pure_URL'] = df['Stats_Access_Link'].apply(extract_url)

# Display the resulting DataFrame
print(df[['Device_Type', 'Pure_URL']])
