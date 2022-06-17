import random
#for counter in range(7,12):2
 #print("The counter is",counter)

#word="Hello"
#for counter in range(0,len(word)):
 # print("Letter",counter,"is",word[counter])

#Sqaure challenge
#for number in range(1,20):
   #print(number*number)

#9 green bottles challenge
#num=int(input("Enter the amount of bottles:")) +1 
#for number in range(num):
 # print(number,"green bottles sitting on the wall")

#times table challenge 1
#num=int(input("Enter a number between 1 ande 12: "))
#for number in range(1,13):
 # print(number*num)

#Fibonacci sequence 
#num1=1
#num2=1
#num3=0
#print(num1)
#print(num2)
#for sequence in range(1,21):
  #num1=num2
  #num2=num3
  #num3=num2+num1  
 # print(num3)    

#Average calculator challenge
#num_count=int(input("Enter how many #numbers you want averaged: "))
#total=0
#for counter in range(num_count):
 # numbers=int(input("Enter a number #you want averaged: "))
#  total=numbers+total
#print(total)
#print(total/num_count)

#FizzBuzz challenge
#i=1
#for counter in range(1,101):
  #if i%3==0 and i%5==0:
   # print("FizzBuzz")
  #elif i%3==0:
   # print("Fizz")
  #elif i%5==0:
   # print("Buzz")
  #else:
   # print(i)
  #i=i+1  

#Times Table challlenge 2
#num1=0
#num2=0
#for counter in range(1,11):
  #num1=random.randint(1,9)
  #num2=random.randint(1,9)
  #print(num1,"*",num2)
  #answer=int(input())
  #if answer == num2*num1:
   # print("correct")
  #else:
   # print("incorrect")

#ROT13
#encoded=""
#text=input("Enter something to be converted to ROT13: ")
#for counter in text:
#  cipher=ord(counter)
#  cipher=cipher +13
#  if cipher >122:
#    cipher=cipher-122+96
#  encoded=encoded+chr(cipher)
#print(encoded)
#encoded=""
#Cipher=input("Enter something to be converted to plain english: ")
#for counter in Cipher:
  #Text=ord(counter)
  #Text=Text -13
  #if Text<97:
  #  Text=Text+122-96
 # encoded=encoded+chr(Text)
#print(encoded)

#Letter game challenge
#text=input("Enter your word: ")
#score =0
#c_score=0
#for counter in text:
  #if counter == "a":
   # c_score =2
  #if counter == "b":
   # c_score =17
  #if counter == "c":
  #  c_score =10
  #if counter == "e":
  #  c_score =12
  #if counter == "e":
  #  c_score =1
  #if counter == "f":
  #  c_score =18
  #if counter == "g":
  #  c_score =16
  #if counter == "h":
  #  c_score =15
  #if counter == "i":
  #  c_score =4
  #if counter == "j":
  #  c_score =25
  #if counter == "k":
   # c_score =21
  #if counter == "l":
#    c_score =9
  #if counter == "m":
  #  c_score =14
  #if counter == "n":
  #  c_score =7
  #if counter == "o":
  #  c_score = 5
  #if counter == "p":
 #   c_score = 13
  #if counter == "q":
   # c_score = 26
  #if counter == "r":
   # c_score = 3
  #if counter == "s":
   # c_score = 8 
  #if counter == "t":
   # c_score = 6
  #if counter == "u":
  #  c_score = 11
  #if counter == "v":
   # c_score = 22
  #if counter == "w":
  #  c_score = 20
  #if counter == "x":
  #  c_score = 23
  #if counter == "y":
  # c_score = 19
  #if counter == "z":
   # c_score = 24
 # score=score+c_score  
#print("You scored",score)

  
  
  
