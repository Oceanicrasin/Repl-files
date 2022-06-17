import random
#Get user input
#number1=float(input("Enter first number: "))
#number2=float(input("Enter second number: "))
#Make calculations
#power_of_result = number1 * number2
#division_result = number1 / number2
#integer_division_result = number1 // number2
#modulus_result = number1 % number2
#Output results
#print()
#print(number1,"to the power of",number2,"is",power_of_result)
#print(number1,"divided by",number2,"is",division_result)
#print(number1,"divided by",number2,"is",integer_division_result)
#print(number1,"divided by",number2,"has a remainder of",modulus_result)


#Roll the dice
#random_number = random.randint(1,6)
#print("You rolled a",random_number)

#RPG challenge
#sides=int(input("How many sides do you want your dice to have? "))
#random_number=random.randint(1,sides)
#print("You rolled a",random_number)

#divisible challenge
#num1=int(input("input a number to be divided: "))
#num2=int(input("input the number you want to divide by:"))
#if num1%num2 ==0:
#  print(num1/num2)
#else:
 # print(num1%num2)

#month challenge
#month = int(input("Enter a number between one and twelve: "))
#if month == 1:
 # print("January has 31 days ")
#elif month == 2:
 # print("February has 28 or 29 days")
#elif month == 3:
 # print("March has 31 days")
#elif month == 4:
 # print("April has 30 days")
#elif month == 5:
 # print("May had 31 days")
#elif month == 6:
 # print("June has 30 days")
#elif month == 7:
 # print("July has 31 days")
#elif month == 8:
 # print("August has 31 days")
#elif month == 9:
 # print("September has 30 days")
#elif month == 10:
 # print("October has 31 days")
#elif month == 11:
 # print("November has 30 days")
#elif month == 12:
 # print("December has 31 days")

#Dice game challenge
num1=random.randint(1,6)
num2=random.randint(1,6)
num3=random.randint(1,6)
if num1 ==num2==num3:
  print(num1+num2+num3)
elif num1==num2:
  print(num1+num2-num3)
elif num1 == num3:
  print(num1+num3-num2)
elif num2 == num3:
  print(num2+num3-num1)
else:
  print(0)