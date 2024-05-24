def check_availability(cart, inventory):

    if(cart.produto in inventory and len(inventory.produto)>=1):
        return True

    else:
        return False