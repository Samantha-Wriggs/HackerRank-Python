import math

AB = float(input())
BC = float(input())

result = str(round(math.degrees(math.atan((AB / 2) / (BC / 2))))) + "°"
print(result)
