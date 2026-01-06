import random
rand= random.randint(10000,99999)
zahl= int(input(" das passwort besteht aus fünf zahlen, kannst du das passwort erraten? \n"))
if rand==zahl:
 print ("das paswort ist richtig")
elif len(str(zahl))!=5:
 print("das passwort besteht aus nur fünf zahlen!")
else:
 print(f"leider isr das passwort {rand}")
