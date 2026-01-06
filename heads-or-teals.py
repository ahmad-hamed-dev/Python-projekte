import random
print("""
welcome to the coin gussing game!
choose a method to toss the coin:

1. using random.random()

2. using random.randint()
""")
choice= input("enter your choice (1 or 2): ")

if choice !="1" and choice !="2":
 print("invalid choice, please enter 1 or 2")

elif choice =="1":

 user_answer=input("enter your choice (heads or tails)):").lower()

 if user_answer !="heads" and user_answer!="tails":
  print("please enter heads or tails")
 else:

  if  random.random() ==0.5:
   print("heads")
  else:
   print("tails")

elif choice=="2":

 user_answer =input("heads or tails? ").lower()
 if user_answer !="heads" and user_answer!="tails":
    print("please enter heads or tails")
 else:
  if  random.randint(0,1) ==0:
   print("heads")
  else:
   print("tails")
