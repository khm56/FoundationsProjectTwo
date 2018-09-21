# CLASSES AND METHODS
class Store():
    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        # your code goes here!
        self.name=name
        self.products=[]

    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        # your code goes here!
        self.products.append(product)

    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        # your code goes here!
        for item in self.products:
            item.__str__()


class Product():
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        # your code goes here!
        self.name=name
        self.description=description
        self.price=price

    def __str__(self):
        # your code goes here!
        print("**Name: %s \nDescription: %s \nPrice: KD %s" %(self.name, self.description, str(self.price)))


class Cart():
    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        # your code goes here!
        self.products=[]

    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        # your code goes here!
        self.products.append(product)

    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        # your code goes here!
        total=0.0
        for item in self.products:
            total+=item.price
        return total

    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        # your code goes here!
        print("\nHere's your receipt:")
        for item in self.products:
            print("\n**Product Name: %s \nDescription: %s \nPrice: %s KWD" %(item.name,item.description,str(item.price)))
        print("Your total price is: KD%s" %(str(self.get_total_price())))

    def checkout(self):
        """
        Does the checkout.
        """
        # your code goes here!
        self.print_receipt()
        confirm=input("Confirm?(yes/no) ")
        confirm=confirm.lower()
        if confirm=="yes":
            print("Your order is confirmed")
        elif confirm=="no":
            print("Your order has been discarded")
        else:
            print("Invalid Input")
            self.checkout()
        return

