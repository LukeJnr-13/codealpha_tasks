"""
Task 2: Stock Portfolio Tracker

The user enters stock symbols and quantities. The program looks up each
price in a hardcoded dictionary, calculates the total investment, and
saves the result to a text file.
"""

# Hardcoded stock prices (in dollars)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130,
}


def get_portfolio():
    """Asks the user for stocks and quantities. Returns {symbol: quantity}."""
    portfolio = {}

    print("Available stocks:", ", ".join(STOCK_PRICES))
    print("Enter a stock symbol and quantity. Type 'done' when finished.\n")

    while True:
        symbol = input("Stock symbol (or 'done'): ").strip().upper()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"  '{symbol}' is not in the price list. Try again.")
            continue

        quantity_text = input(f"  How many shares of {symbol}? ").strip()

        if not quantity_text.isdigit() or int(quantity_text) <= 0:
            print("  Please enter a whole number greater than 0.")
            continue

        # If the same stock is entered twice, add to the existing quantity
        portfolio[symbol] = portfolio.get(symbol, 0) + int(quantity_text)

    return portfolio


def calculate_total(portfolio):
    """Returns the total value of the portfolio."""
    total = 0
    for symbol, quantity in portfolio.items():
        total += STOCK_PRICES[symbol] * quantity
    return total


def build_report(portfolio, total):
    """Builds the summary text shown on screen and saved to the file."""
    lines = ["--- Portfolio Summary ---"]
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        lines.append(f"{symbol}: {quantity} shares x ${price} = ${value}")
    lines.append("-------------------------")
    lines.append(f"Total investment: ${total}")
    return "\n".join(lines)


def save_report(report, filename="portfolio.txt"):
    """Saves the report to a text file."""
    with open(filename, "w") as file:
        file.write(report + "\n")
    print(f"\nResult saved to {filename}")


def main():
    portfolio = get_portfolio()

    if not portfolio:
        print("No stocks entered. Goodbye!")
        return

    total = calculate_total(portfolio)
    report = build_report(portfolio, total)

    print("\n" + report)

    choice = input("\nSave this to a file? (y/n): ").strip().lower()
    if choice == "y":
        save_report(report)


if __name__ == "__main__":
    main()
