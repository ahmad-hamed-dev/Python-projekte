ort= input("wählen Sie bitte den Ort aus: Berlin,sachsen-anhalt oder Sachsen \n")
if ort.lower() == "berlin":
 print("Sie haben Berlin ausgewählt")
elif ort.lower() == "sachsen-anhalt":
  print("Sie haben Sachsen-Anhalt ausgewählt")
elif ort.lower() == "sachsen":
 print("Sie haben Sachsen ausgewählt")
else:
  print(f"entschuldigung, wir haben keine {ort} auf unserer Liste")
alt=int(input("wie Alt sind Sie? \n"))
führerschein=input("haben Sie einen Führerschein? (yes/no) \n").lower()
if alt>=18 and führerschein== "yes":
 print("Sie können das Auto mieten")
elif alt<18 or führerschein== "no":
 print("leider können Sie nicht das Auto mieten")
