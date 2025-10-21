stock_prices={"AAPL":180,"TSLA":250,"GOOGL":130,"MSFT":300,"AMZN":140}
portfolio={}
print("=== Simple Stock Portfolio Tracker")
print("Available Stocks:",",".join(stock_prices.keys()))
n=int(input("how many different stocks do you own:"))
for i in range(n):
    stock=input(f"enter stock name #{i+1}:").upper()
    qty=int(input(f"enter quantity of {stock}:"))
    if stock in stock_prices:
        portfolio[stock]=qty
    else:
        print("stock not found in price list")
total_investment=0
for stock,qty in portfolio.items():
    value=stock_prices[stock]*qty
    print(f"{stock}->{qty} shares*${stock_prices[stock]}=${value}")
    total_investment+=value
print("\nTotal Portfolio Value:$",total_investment )
with open("portfolio_summary.txt","w")as f:
    f.write("stock portfolio summary\n")
    for stock,qty in portfolio.items():
        f.write(f"{stock}:{qty} * ${stock_prices[stock]}=${stock_prices[stock]*qty}\n")
        f.write(f"\n Total Value:${total_investment}")
print("\nportfolio summary saved to 'portfolio_summary.txt")
        