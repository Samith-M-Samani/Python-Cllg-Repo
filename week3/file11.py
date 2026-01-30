# 11. Highest Selling Product
# Problem:
# You are given a list of tuples where each tuple represents (product_name, quantity_sold). Return the product name with the highest total sales.
# Input:
# [("Pen", 10), ("Pencil", 25), ("Pen", 15)]
# Output:
# "Pen"
def findHighestSelling(sales):
    sales_dict = {}
    for product, quantity in sales:
        if product in sales_dict:
            sales_dict[product] += quantity
        else:
            sales_dict[product] = quantity
    highest_selling_product = max(sales_dict, key=sales_dict.get)
    return highest_selling_product
def main():
    sales = [("Pen", 10), ("Pencil", 25), ("Pen", 15)]
    result = findHighestSelling(sales)
    print(result)  
if __name__ == "__main__":
    main()