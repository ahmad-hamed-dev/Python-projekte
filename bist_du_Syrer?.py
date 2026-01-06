print("welkommen in test (bist du syrer?)")

f1=input("du bist jetzt auf der strasse, du willst nach mazza gehen, fährst du mit dem bus oder mit taxi? \n").lower()
if f1=="bus":
 print ("der schafft das niemals, du bist kein syrer")
elif f1=="taxi":
 print("toll")
 f2=input("willst du mit der karte oder casch bezahlen? (karte/casch) \n").lower()
 if f2=="karte":
   print("es gibt keine karte in syrien, du bist kein syrer")
 elif f2=="casch":
   print("toll, du bist syrer")
 else :
  print("falsche antwort")
else:
 print("falsch, bitte wählst du eine beide wahlen!")
