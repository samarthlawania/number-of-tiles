L = float(input("Enter the length of floor"))
W = float(input("Enter the width of floor"))
l = float(input("Enter the length of tile"))
w = float(input("Enter the width of tile"))
Area_of_floor = L * W
Area_of_tile = l * w
N = Area_of_floor / Area_of_tile
print(f"The number of tiles required is {N}")
