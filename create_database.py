import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect('casino_campaigns.db')
cursor = conn.cursor()

# Create a table for campaign data
cursor.execute('''
CREATE TABLE IF NOT EXISTS campaigns (
    id INTEGER PRIMARY KEY,
    campaign_type TEXT,
    date TEXT,
    customer_response INTEGER,
    revenue_generated REAL,
    geo_location TEXT
)
''')

# Sample data
campaigns_data = [
    ('Email', '2024-01-01', 50, 5000.0, 'New York'),
    ('Direct Mail', '2024-01-15', 30, 3000.0, 'California'),
    ('Telemarketing', '2024-02-01', 70, 7000.0, 'Nevada'),
    ('Email', '2024-02-15', 60, 6000.0, 'Florida'),
    ('Direct Mail', '2024-03-01', 40, 4000.0, 'Texas'),
]

# Insert sample data
cursor.executemany('''
INSERT INTO campaigns (campaign_type, date, customer_response, revenue_generated, geo_location)
VALUES (?, ?, ?, ?, ?)
''', campaigns_data)

# Commit changes and close connection
conn.commit()
conn.close()

print("Database and sample data created successfully.")
