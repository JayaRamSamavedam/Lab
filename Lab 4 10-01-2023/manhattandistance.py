def manhattan_distance(point1, point2):
    return sum(abs(value1 - value2) for value1, value2 in zip(point1, point2))
x1 = (1,2,3,4,5,6)
x2 = (10,20,30,1,2,3)
print(manhattan_distance(x1, x2))