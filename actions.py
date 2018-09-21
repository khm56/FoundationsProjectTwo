# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "www.ishop.com"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    print()
    for item in stores:
        print("- %s" %(item.name))

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!
    for item in stores:
        if store_name==item.name:
            return item
    return False

def pick_store(cart):
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!
    print_stores()
    print("Pick a store by typing its name. Or type \"checkout\" to pay your bills and say your goodbyes.")
    selected=input()
    if selected == "checkout":
        cart.checkout()
    elif get_store(selected) == False:
        print("No store with that name. Please try again")
        pick_store(cart)
    else:
        pick_products(cart,get_store(selected))




def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    # your code goes here!
    print(picked_store.name)
    picked_store.print_products()
    print("\nPick the items you'd like to add in your cart by typing the product name exactly as it was spelled above.\n Or type \"back\" to go back ")
    while True:
        prod=input()
        if prod == "back":
            break
        else:
            for items in picked_store.products:
                if prod == items.name:
                  cart.add_to_cart(items)
    pick_store(cart)


def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    # your code goes here!
    pick_store(cart)


def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
