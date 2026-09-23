class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price 
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

class Bill:
    def __init__(self):
        self.product = []

    def add_product(self, product):
        self.product.append(product)

    def calculate_total(self):
        total = 0

        for product in self.product:
            total += product.total_price()

        return total

    def calculate_tax(self, total):
        tax = total * 0.05
        return tax

    def display_bill(self):
        print("\n===== BILL =====")
        print(f"{'Product':<15}{'Price':<10}{'Qty':<10}{'Total':<10}")
        print("-" * 45)

        for product in self.product:
            print(f"{product.name:<15}{product.price:<10}{product.quantity:<10}{product.total_price():<10.2f}")

        total = self.calculate_total()
        tax = self.calculate_tax(total)
        final_total = total + tax

        print("-" * 45)
        print("Subtotal:", total)
        print("Tax (5%):", tax)
        print("Final Total:", final_total)

# Creating products
product1 = Product("Laptop", 50000, 1)
product2 = Product("Mouse", 500, 2)
product3 = Product("Keyboard", 1000, 1)

# Creating bill
bill = Bill()

# Adding products to bill
bill.add_product(product1)
bill.add_product(product2)
bill.add_product(product3)

# Display final bill
bill.display_bill()
