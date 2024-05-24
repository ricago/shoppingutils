def apply_discoubt(cart, discount):
    for i in range(cart.produto):
        cart.produto[i] * (1-(0.1*discount))