stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 350,
    "AMZN": 170
}

total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")

while True:
    stock = input("\nEnter Stock Name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    quantity = int(input("Enter Quantity: "))

    investment = stock_prices[stock] * quantity
    total_investment += investment

    print(f"Investment in {stock}: ${investment}")

print("\n===== PORTFOLIO SUMMARY =====")
print("Total Investment Value: $", total_investment)

with open("portfolio_report.txt", "w") as file:
    file.write(f"Total Investment Value: ${total_investment}")

print("Portfolio report saved successfully!")