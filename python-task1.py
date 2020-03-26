def calcArea (radius):
    return 3.142 * radius ** 2;

radius = int(input("Enter radius to calculate for area :"))
result = calcArea(radius)

print(result)