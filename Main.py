class Provider:

    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def show(self):

        print(f"Provider: {self.name} | Rating: {self.rating}/5")


class Service:

    def __init__(self, name, price, provider):

        self.name = name

        self.price = price

        self.provider = provider

    def show(self):

        print(f"{self.name} - ${self.price}")

        self.provider.show()

class HouseServiceApp:

    def __init__(self):

        self.services = [

            Service("Plumber", 50, Provider("Rajat", 4.7)),

            Service("Electrician", 80, Provider("karan", 4.6)),

            Service("Cleaner", 30, Provider("Sarthak", 4.9))

        ]

        self.cart = []

    def show_services(self):

        for i, s in enumerate(self.services):

            print(f"\n{i+1}. ", end=""); s.show()

    def add_to_cart(self, idx):

        self.cart.append(self.services[idx])

        print("Added to cart.")


    def show_cart(self):

        if not self.cart: print("Cart empty"); return

        for s in self.cart: s.show()


    def checkout(self):

        total = sum(s.price for s in self.cart)

        print(f"Total = ${total}")

app = HouseServiceApp()

while True:

    print("\n---House Services---")

    print("1. Show Services")

    print("2. Add Service to Cart")

    print("3. View Cart")

    print("4. Checkout")

    print("5. Exit")

    c = input("Choice: ")

    if c == "1": app.show_services()

    elif c == "2":

        app.show_services()

        n=int(input("Select service number")) - 1

        app.add_to_cart(n)

    elif c == "3": app.show_cart()

    elif c == "4": app.checkout()

    elif c == "5": break 

