import math
def canMeasureWater(x: int, y: int, z: int) -> bool:
    return False if x + y < z else True if x + y == 0 else not z % math.gcd(x, y)
print(canMeasureWater(3,5,4))