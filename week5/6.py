prices = [100, 250, 500, 750, 1000]
print("Original Prices:", prices)
final_prices = list(map(lambda x: x + (x * 0.18), prices))
print("Final Prices after 18% GST:")
for price in final_prices:
    print(round(price, 2))