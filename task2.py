class StockPortfolio:
    def __init__(self):
        self.portfolio = {}
        self.stock_prices = {
            'AAPL': 150.00,   # Apple
            'GOOGL': 2800.00, # Google
            'AMZN': 3400.00,  # Amazon
            'TSLA': 700.00,   # Tesla
            'MSFT': 300.00    # Microsoft
        }

    def add_stock(self, symbol, quantity):
        """Add a stock to the portfolio."""
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity
        print(f"Added {quantity} shares of {symbol}.")

    def remove_stock(self, symbol, quantity):
        """Remove a stock from the portfolio."""
        if symbol in self.portfolio:
            if quantity >= self.portfolio[symbol]:
                del self.portfolio[symbol]
                print(f"Removed all shares of {symbol}.")
            else:
                self.portfolio[symbol] -= quantity
                print(f"Removed {quantity} shares of {symbol}.")
        else: 
            print(f"{symbol} is not in your portfolio.")

    def fetch_stock_price(self, symbol):
        """Fetch the current stock price from hardcoded values."""
        # Simulate fetching price from a data source
        return self.stock_prices.get(symbol, None)

    def track_performance(self):
        """Track and display the portfolio performance."""
        print("\nPortfolio Performance:")
        total_value = 0
        for symbol, quantity in self.portfolio.items():
            price = self.fetch_stock_price(symbol)
            if price is not None:
                stock_value = price * quantity
                total_value += stock_value
                print(f"{symbol}: {quantity} shares x ${price:.2f} = ${stock_value:.2f}")
            else:
                print(f"Price for {symbol} not available.")
        print(f"\nTotal Portfolio Value: ${total_value:.2f}")

def main():
    portfolio = StockPortfolio()
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Track Performance")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            portfolio.add_stock(symbol, quantity)
        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity to remove: "))
            portfolio.remove_stock(symbol, quantity)
        elif choice == '3':
            portfolio.track_performance()
        elif choice == '4':
            print("Exiting Portfolio Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
