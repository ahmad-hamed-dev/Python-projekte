print("welcome to place the rabbit\n")
place=[  [["🦗"], ["🦗"], ["🦗"] ], [["🦗"], ["🦗"], ["🦗"]] ,[ ["🦗"], ["🦗"], ["🦗"]  ]]
print(f"{place[0]} \n{place[1]} \n{place[2]}")


print("\nwhere should the rabbit🐇 go?")
position=input("please choose a row and a column... ")


row=int(position[0])
column=int(position[1])
place[row-1][column-1]="🐇"

print("\n succes ...\n")
print(f"{place[0]} \n{place[1]} \n{place[2]}")
