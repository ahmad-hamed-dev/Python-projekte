
print("""
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝
""")
print("""
wilkommen zu meine insel
es gibt zwei türen vor dir, eine rote tür 🚪 und eine blaue tür 🚪
""")
tür=input("whelche tür willst du öffnen? (rot/blau) ").lower()
print(" ")
if tür == "rot":
 print("wünderbar, du hast die richtige tür gewählt")
 print("du findest drei kisten vor dir, eine goldene kiste🎁, eine silberne kiste🎁, und eine bronzene kiste🎁")
 kiste=input("whelche kiste willst du öffnen? (golden/silber/bronze)").lower()

 if kiste.lower()=="golden" or kiste =="silber":
  print("du hast die schlangenkiste gewählt 🐍🐍🐍 , du bist gestorben")
 elif kiste =="bronze":
  print(" ")
  print("du hast die schatzkiste gewählt 🪙🪙🪙, du hast gewonnen") 
 else:
  print("das geht nicht")

elif tür =="blau":
 print("schade, du hast die falsche tür gewählt")
 
else:
 print("das geht nicht, bitte wählst du eine beide türen!")
