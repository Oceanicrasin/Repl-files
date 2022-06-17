#Mayan calender
# date=input("Enter the date that you want to convert to Mayan speerated by a space: ")

# i=0
# dateList=date.split()
# day=int(dateList[0])
# month=int(dateList[1])
# year=int(dateList[2])
# dayCount=day
# if month == 2:
#   dayCount=dayCount+31
# elif month == 3:
#   dayCount = dayCount+59
# elif month == 4:
#   dayCount = dayCount+90
# elif month == 5:
#   dayCount=dayCount+120
# elif month == 6:
#  dayCounnt=dayCount+151
# elif month == 7:
#   dayCount=dayCount+181
# elif month == 8:
#   dayCount=dayCount+212
# elif month == 9:
#   dayCount=dayCount+243
# elif month == 10:
#   dayCount=dayCount+273
# elif month == 11:
#   dayCount = dayCount+304
# elif month == 12:
#   dayCount=dayCount+334

# if year%4 == 0 and month!=2 and month!=1:
#   dayCount=dayCount+1
 
# leaps=(year-1)/4
# leaps=int(leaps)
# dayCount=dayCount+((year-1)*365)+leaps
# dayCount=dayCount+1288708
# print(dayCount)
# kin = 0
# uinal=0
# tun=0
# katun=0
# baktun=0
# kin = 0
# uinal=0
# tun=0
# katun=0
# baktun=0
# kin=dayCount
# #print(dayCount)
# i=0
# while kin>144000:
#   kin=kin-144000
#   baktun=baktun+1
#   i=i+1
# while kin>7200:
#   kin=kin-7200
#   katun=katun+1
# while kin>360:
#   kin=kin-360
#   tun=tun+1
# while kin>20:
#   kin=kin-20
#   uinal=uinal+1
# print(f"{baktun}-{katun}-{tun}-{uinal}-{kin}")

#Parser challenge
# while True:
#   add=False
#   minus=False
#   multiply=False
#   divide=False
#   calculation=input("Enter your calculation: ")
#   i=0
#   for counter in calculation:
#     if counter == "+":
#       operatorLocation=calculation.find("+")
#       add=True
#       break
#     elif counter == "-":
#        operatorLocation=calculation.find("-")
#        minus=True
#        break
#     elif counter =="*":
#       operatorLocation=calculation.find("*")
#       multiply = True
#       break
#     elif counter == "/":
#       operatorLocation=calculation.find("/")
#       divide = True
#       break
#     i=i+1
  
#   firstNumber=int(calculation[0:operatorLocation])
#   secondNumber=int(calculation[operatorLocation+1:len(calculation)])
  
#   print("firstNumber, %+d" %firstNumber )
#   print("secondNumber, %+d" %secondNumber)
#   if add:
#     print(firstNumber+secondNumber)
#   if minus:
#     print(firstNumber-secondNumber)
#   if multiply:
#     print(firstNumber*secondNumber)
#   if divide:
#     print(firstNumber/secondNumber)
  
#  Change Calculator
# while True:
#   amount=float(input("Enter how much change you need: "))
#   fiftyPound=0
#   twentyPound=0
#   tenPound=0
#   fivePound=0
#   twoPound=0
#   onePound=0
#   fiftyPence=0
#   twentyPence=0
#   tenPence=0
#   fivePence=0
#   twoPence=0
#   onePence=0
#   while amount>=50:
#     amount=amount-50
#     fiftyPound=fiftyPound+1

#   while amount>=20:
#     amount = amount - 20
#     twentyPound=twentyPound+1

#   while amount >=10:
#     amount=amount-10
#     tenPound=tenPound+1

#   while amount>=5:
#     amount=amount-5
#     fivePound=fivePound+1
    
#   while amount>=2:
#     amount=amount-2
#     twoPound=twoPound+1
    
#   while amount>=1:
#     amount=amount-1
#     onePound=onePound+1
  
#   while amount>=0.50:
#     amount=amount-0.50
#     fiftyPence=fiftyPence+1
  
#   while amount>=0.20:
#     amount=amount-0.20
#     twentyPence=twentyPence+1
  
#   while amount>=0.10:
#     amount=amount-0.10
#     tenPence=tenPence+1
  
#   while amount>=0.05:
#     amount=amount-0.05
#     fivePence=fivePence+1
  
#   while amount>=0.02:
#     amount=amount-0.02
#     twoPence=twoPence+1
    
#   while amount>0.009:
#     amount=amount-0.01
#     onePence=onePence+1
#   print("number of £50:",fiftyPound)
#   print("number of £20:",twentyPound)
#   print("Number of £10:",tenPound)
#   print("number of £5: ",fivePound)
#   print("number of £2: ",twoPound)
#   print("number of £1: ",onePound)
#   print("number of 50p:",fiftyPence)
#   print("number of 20p:",twentyPence)
#   print("number of 10p:",tenPence)
#   print("number of 5p: ",fivePence)
#   print("number of 2p: ",twoPence)
#   print("number of 1p: ",onePence)

#London underground challenge
# def london_underground_challenge():
#   while True:
#     letters=[]
#     text_file=open("Stations.txt","r")
#     Check=input("Enter a word: ")
#     print()
#     for counter in Check:
#         letters.append(counter.upper())
#       #  letters.append(counter)
#    # print(letters)
#     while True:
#       display=True
#       station_letters=[]
#       a=text_file.readline()
#       for counter in a:
#         station_letters.append(counter.upper())
#        # print('Aloha',station_letters)
#       for counter in letters:
#         if counter in station_letters:
#           display=False
#       if display == True:
#         print(a)
#       if not a:break 

# functionreference = london_underground_challenge

# functionreference()

    
    
