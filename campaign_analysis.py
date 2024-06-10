import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite database
print("Connecting to the database...")
conn = sqlite3.connect('venv/casino_campaigns.db')

# Query the data
print("Querying the data...")
query = '''
SELECT campaign_type, date, customer_response, revenue_generated, geo_location
FROM campaigns
'''
df = pd.read_sql_query(query, conn)
conn.close()

# Display basic statistics
print("Displaying basic statistics...")
print(df.describe())

# Check if data is loaded correctly
print("Displaying data preview...")
print(df.head())

# Average revenue by campaign type
print("Calculating average revenue by campaign type...")
revenue_by_type = df.groupby('campaign_type')['revenue_generated'].mean()
print("Average revenue by campaign type:")
print(revenue_by_type)

# Average customer response by campaign type
print("Calculating average customer response by campaign type...")
response_by_type = df.groupby('campaign_type')['customer_response'].mean()
print("Average customer response by campaign type:")
print(response_by_type)

# Correlation between customer response and revenue
print("Calculating correlation between customer response and revenue...")
correlation = df[['customer_response', 'revenue_generated']].corr()
print("Correlation matrix:")
print(correlation)

# Plot Average Revenue by Campaign Type
print("Plotting average revenue by campaign type...")
plt.figure(figsize=(10, 6))
revenue_by_type.plot(kind='bar', color='skyblue')
plt.xlabel('Campaign Type')
plt.ylabel('Average Revenue ($)')
plt.title('Average Revenue by Campaign Type')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('average_revenue_by_campaign_type.png')
plt.show()

# Plot Average Customer Response by Campaign Type
print("Plotting average customer response by campaign type...")
plt.figure(figsize=(10, 6))
response_by_type.plot(kind='bar', color='lightgreen')
plt.xlabel('Campaign Type')
plt.ylabel('Average Customer Response')
plt.title('Average Customer Response by Campaign Type')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('average_response_by_campaign_type.png')
plt.show()

# Scatter plot for Revenue vs Customer Response
print("Plotting revenue vs customer response...")
plt.figure(figsize=(10, 6))
plt.scatter(df['customer_response'], df['revenue_generated'], color='coral')
plt.xlabel('Customer Response')
plt.ylabel('Revenue Generated ($)')
plt.title('Revenue vs Customer Response')
plt.tight_layout()
plt.savefig('revenue_vs_response.png')
plt.show()

# Save the analyzed data to a CSV file
df.to_csv('campaign_data_summary.csv', index=False)

print("Analysis complete. Plots saved and data exported to CSV.")
