products = (("Pen", 10, 25), ("Notebook", 50, 12), ("Pencil", 5, 40))
print("Product catalogue")
total_value = 0
for product in products:
    name = product[0]
    price = product[1]
    quantity = product[2]
    value = price * quantity
    total_value = total_value + value
    print(name, "- price:", price, "quantity:", quantity, "stock value:", value)
print("Total stock value:", total_value)
