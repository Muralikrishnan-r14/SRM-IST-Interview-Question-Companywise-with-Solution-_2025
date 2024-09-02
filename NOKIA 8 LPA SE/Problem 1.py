def orderpizza(orderplaced,size):
    ordered_pizza = []
    for i in range(size):
        if orderplaced[i] <= -1:
            ordered_pizza.append(orderplaced[i])
        else:
            if ordered_pizza[len(ordered_pizza)-1] != 0:
                ordered_pizza.append(0)
    return ordered_pizza
orderplaced=[-44,5,-99,99,86,3,-88,-55,-77]
size=len(orderplaced)
print(orderpizza(orderplaced, size))