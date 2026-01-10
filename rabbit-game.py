print("welcome to place the rabbit:\n")
field= ["🌿","🌿","🌿"],["🌿","🌿","🌿"],["🌿","🌿","🌿"]
print(f"{field[0]} \n{field[1]} \n{field[2]}")
print("where should the rabbit go?")
position=input("please choose a row and a column:... ")

row= int(position[0])
column= int(position[1])
field[row-1][column-1]= "🐇"
print("\nsuccess...\n")

print(f"{field[0]} \n{field[1]} \n{field[2]}")
