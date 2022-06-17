import random
guessCount=1
while True:
  try:
    diff=input("Do you want hard, normal or easy difficulty: \n ")
    if diff == "hard" or diff == "normal" or diff == "easy":
      break
  except:
    print("Invalid data try again")
if diff == "hard":
  numberSize=5
else:
  numberSize=4
numbers=[random.randint(1,9)]
sNumbers=str(numbers[0])
for counter in range(numberSize-1):
  number=random.randint(0,9)
  numbers.append(number)
  sNumbers=sNumbers+str(number)
print(sNumbers)
correct=False
while correct == False:
  while True:
    print("Rounds",guessCount)
    try:
      pChoice=input(f"Enter your {numberSize} digit number guess: ")
      pChoiceL=[]
      for counter in pChoice:
        pChoiceL.append(counter)
      if pChoice == sNumbers:
        print("Correct")
        correct=True
      else:
        if diff == "easy":
          positions=[]
          i=0
          ii=0
          for counter in range(4):
            if int(pChoiceL[i])==numbers[i]:
              positions.append(i+1)
              ii=ii+1
            i=i+1
          print(f"You have {ii} numbers correct")  
          if positions:
            print("The positons are",positions)
          
        elif diff == "normal" or diff == "hard":  
          i=0
          ii=0
          for counter in range(numberSize):
            if int(pChoiceL[i])==numbers[i]:
              ii=ii+1
            i=i+1
          print(f"You have {ii} numbers correct")  
      guessCount=guessCount+1          
      break
    except:
      print("Invalid data try again")
