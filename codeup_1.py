def getLowestPrice(arrayPrice):
    lowestPrice = None
    for price in arrayPrice:
        if lowestPrice is None:
            lowestPrice = price
        else:
            if int(lowestPrice) > int(price):
                lowestPrice = price
    return lowestPrice

pastaPrice = [input() for _ in range(3)]
juicePrice = [input() for _ in range(2)]

lowestPastPrice = getLowestPrice(pastaPrice)
lowestJuicePrice = getLowestPrice(juicePrice)

sumPrice = float(lowestPastPrice) + float(lowestJuicePrice)
totalPrice = float(sumPrice) + float(sumPrice)/10

print(totalPrice)

