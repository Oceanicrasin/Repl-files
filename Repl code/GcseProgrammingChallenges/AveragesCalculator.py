end = False
personList=[]
add=int(input("Enter a number to add to your list \n")) 
personList.append(add)
while end == False:
  choice=int(input("Type 1 to print calculations or 2 to continue entering: "))
  if choice == 2:
    add=int(input("Enter a number to add to your list \n")) 
    personList.append(add)
  else:
    break
mean=0
median=0
mode=[]
personList.sort()
i=0
for counter in personList:
  if i!=0:
    if personList[i]==personList[i-1]:
      mode.append(personList[i])
  mean=mean+counter
  i=i+1
mean=mean/len(personList)
print(personList)
if not mode:
  print("There is no mode")
else:
  print("Mode",mode)
print("Mean: ",mean)
length=len(personList)
if length%2==0:
  firstNumber=personList[int(length/2)]
  secondNumber=personList[int(length/2+1)]
  median=(firstNumber+secondNumber)/2
else:
  median=personList[int(length/2)]
print("Median", median)  