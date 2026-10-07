def main():

    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 330,
        "AMZN": 145,
    }

    portfolio = []

    print("--- Stock Portfolio Tracker ---") 

    # Collect user investments
    while True:
        symbol = input("\nEnter stock symbol (e.g., AAPL): ").strip().upper()

        if symbol not in stock_prices:
            print(f"'{symbol}' is not available. Try one of: {', '.join(stock_prices.keys())}")
            continue

        try:
            quantity = int(input(f"Enter quantity for {symbol}: "))
            if quantity <= 0:
                print("Quantity must be a positive integer.")
                continue
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        price = stock_prices[symbol]
        total_value = price * quantity

        portfolio.append({
            "symbol": symbol,
            "quantity": quantity,
            "price": price,
            "total": total_value,
        })

        again = input("Add another stock? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            break

    if not portfolio:
        print("\nNo stocks added to portfolio.")
        return

    # Display summary table
    print("\n" + "-" * 45)
    print(f"{'Stock':<10}{'Qty':<10}{'Price ($)':<12}{'Total ($)':<12}")
    print("-" * 45)

    for item in portfolio:
        print(f"{item['symbol']:<10}{item['quantity']:<10}{item['price']:<12}{item['total']:<12}")

    grand_total = sum(item["total"] for item in portfolio)
    top_holding = max(portfolio, key=lambda x: x["total"])

    print("-" * 45)
    print(f"Total Investment   : ${grand_total:,.2f}")
    print(f"Total Unique Stocks: {len(portfolio)}")
    print(f"Largest Holding    : {top_holding['symbol']} (${top_holding['total']:,.2f})")

    # Save summary to file
    save_portfolio_report("portfolio_result.txt", portfolio, grand_total, top_holding)
    print("\nSummary saved to portfolio_result.txt")


def save_portfolio_report(filename, portfolio, grand_total, top_holding):
    """Saves the calculated portfolio details into a readable text file."""
    with open(filename, "w") as file:
        file.write("PORTFOLIO SUMMARY REPORT\n")
        file.write("=" * 35 + "\n\n")

        for item in portfolio:
            file.write(
                f"{item['symbol']}: {item['quantity']} shares @ ${item['price']} = ${item['total']}\n"
            )

        file.write("-" * 35 + "\n")
        file.write(f"Total Investment: ${grand_total:,.2f}\n")
        file.write(f"Largest Holding : {top_holding['symbol']} (${top_holding['total']:,.2f})\n")


if __name__ == "__main__":
    main()