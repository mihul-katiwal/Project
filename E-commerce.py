import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {
    "product": ["Laptop", "Mobile", "Tablet", "Headphones", "Smartwatch"],
    "quantity_sold": [120, 200, 90, 190, 150],
    "price": [60000, 25000, 30000, 5000, 10000]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df["revenue"] = df["quantity_sold"] * df["price"]

df["profit"] = df["revenue"] * 0.20

print("\nUpdated DataFrame:")
print(df)

fig, ax = plt.subplots(3, 3, figsize=(20, 8))

ax[0, 0].plot(df['product'], df['revenue'], marker='o', color='blue')
ax[0, 0].set_title("Revenue Line Chart")
ax[0, 0].set_xlabel("Product")
ax[0, 0].set_ylabel("Revenue")
ax[0, 0].tick_params(axis='x', rotation=10)
ax[0, 0].grid(True)

ax[0, 1].plot(df['product'], df['quantity_sold'], marker='s', color='green')
ax[0, 1].set_title("Quantity Sold Line Chart")
ax[0, 1].set_xlabel("Product")
ax[0, 1].set_ylabel("Quantity")
ax[0, 1].tick_params(axis='x', rotation=10)
ax[0, 1].grid(True)

ax[0, 2].plot(df['product'], df['profit'], marker='^', color='red')
ax[0, 2].set_title("Profit Line Chart")
ax[0, 2].set_xlabel("Product")
ax[0, 2].set_ylabel("Profit")
ax[0, 2].tick_params(axis='x', rotation=10)
ax[0, 2].grid(True)

ax[1, 0].bar(df['product'], df['revenue'], color='orange')
ax[1, 0].set_title("Revenue Bar Chart")
ax[1, 0].set_xlabel("Product")
ax[1, 0].set_ylabel("Revenue")
ax[1, 0].tick_params(axis='x', rotation=10)
ax[1, 0].grid(True)

ax[1, 1].bar(df['product'], df['quantity_sold'], color='skyblue')
ax[1, 1].set_title("Quantity Sold Bar Chart")
ax[1, 1].set_xlabel("Product")
ax[1, 1].set_ylabel("Quantity")
ax[1, 1].tick_params(axis='x', rotation=10)
ax[1, 1].grid(True)

ax[1, 2].bar(df['product'], df['profit'], color='yellow')
ax[1, 2].set_title("Profit Bar Chart")
ax[1, 2].set_xlabel("Product")
ax[1, 2].set_ylabel("Profit")
ax[1, 2].tick_params(axis='x', rotation=10)
ax[1, 2].grid(True)

explode = [0.03] * len(df)
ax[2, 0].pie(
    df["revenue"],
    labels=df["product"],
    autopct="%1.1f%%",
    startangle=90,
    shadow=True,
    explode=explode,
    textprops={'fontsize': 8},
    wedgeprops={
        "width": 0.6,
        "edgecolor": "black"
    }
)

ax[2, 0].set_title("Revenue Pie chart")

explode = [0.03] * len(df)
ax[2, 1].pie(
    df['quantity_sold'],
    labels=df['product'],
    autopct='%1.1f%%',
    shadow=True,
    explode=explode,
    textprops={'fontsize': 8},
    wedgeprops={
        "width": 0.6,
        "edgecolor": "black"
    }
)
ax[2, 1].set_title("Quantity Sold Pie Chart")

explode = [0.03] * len(df)
ax[2, 2].pie(
    df['profit'],
    labels=df['product'],
    autopct='%1.1f%%',
    shadow=True,
    explode=explode,
    textprops={'fontsize': 8},
    wedgeprops={
        "width": 0.6,
        "edgecolor": "black"
    }
)
ax[2, 2].set_title("Profit Pie Chart")

plt.tight_layout()
plt.show()