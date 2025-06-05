# Import modules
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',          # ✅ Usually localhost
    user='root',               # ✅ Replace with your actual username
    password='Sana2003$',  # ✅ Replace with your real password
    database='sales_demo'      # ✅ This must match your DB name
)

# Create cursor
cursor = conn.cursor()

# Query: total quantity and revenue by product
query = """
SELECT 
    product, 
    SUM(quantity) AS total_quantity,
    SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY product;
"""

cursor.execute(query)
results = cursor.fetchall()

# Put results into DataFrame
df = pd.DataFrame(results, columns=["Product", "Total Quantity", "Total Revenue"])

# Print results
print("\nSales Summary:\n")
print(f"Total Quantity Sold: {df['Total Quantity'].sum()}")
print(f"Total Revenue Earned: ₹{df['Total Revenue'].sum():.2f}")
print(df)

# Plot using matplotlib
plt.figure(figsize=(8, 5))
plt.bar(df['Product'], df['Total Revenue'], color='lightgreen')
plt.title("Total Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

# Close connection
cursor.close()
conn.close()



