def squareArea(l):
    return round(l** 2, 4)
side_length = float(input("Side Length: "))
area = squareArea(side_length)
print("Area: " + str(area))
