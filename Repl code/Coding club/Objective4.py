#Using selection statements to check variables
#Ask user for the number
#number = int(input("Enter a number 1-3:"))
#Check the value of the number
#if number == 1: print("Number one")
#if number == 2: print("Number two")
#if number == 3: print("Number three")

#Using logic operators
#choice = input("Enter a number 1-3: ")
#if choice > "0" and choice <"3":
  #print("Valid input")
#else:
 # print("Invalid input")

#Using case selection#Ask user for the number
#print("1. Add numbers")
#print("2. Subtract numbers")
#print("3. Quit")

#Multiple branches depending on selection]
#choice=input("Enter your choice: ")
#if choice == "1":
 # print("Add numbers chosen")
#elif choice == "2":
 #print("Subtract numbers chosen")
#elif choice == "3":
  #print("Quit chosen")

  #Under age challenge
#age = int(input("Enter your age: "))
#if age > 18:
  #print("over 18")
#else:
  #print("under 18")

#water temperature challenge

#waer=int(input("enter the temperature of your water: "))
#if waer <=0:
 # print("You have ice not water. Fool")
#elif waer >=100:
 # print(" You have water vapour not water. Fool")
#else:
  #print("Congrats you actually have water unlike some fools")

#Vocational grade challenge
#grade=int(input("Enter your test score out of 100: "))
#if grade<40:
 # print("Fail")
#elif grade>=80:
 # print("Distinction")
#elif grade>=40 and grade<60:
 # print("Pass")
#elif grade>=60 and grade<80:
  #print("Merit")

# Extended visual dice challenge
#number = int(input("Enter a number on a dice to be outpted: "))
#if number == 1:
  #print( "/ / / / / /")
  #print( "/         /")
  #print( "/    #    /") 
  #print( "/         /")
  #print( "/ / / / / /")
#elif number == 2:
  #print( "/ / / / / /")
  #print( "/#       /")
  #print( "/         /") 
  #print( "/        #/")
  #print( "/ / / / / /")
#elif number == 3:
  #print( "/ / / / / /")
  #print( "/#        /")
  #print( "/    #    /") 
  #print( "/        #/")
  #print( "/ / / / / /")
#elif number == 4:
  #print( "/ / / / / /")
  #print( "/#      #/")
  #print( "/         /") 
  #print( "/#       #/")
  #print( "/ / / / / /")  
#elif number == 5:
  #print( "/ / / / / /")
  #print( "/#       #/")
  #print( "/    #    /") 
  #print( "/#       #/")
  #print( "/ / / / / /")  
#elif number == 6:
  #print( "/ / / / / /")
  #print( "/#       #/")
  #print( "/#       #/") 
  #print( "/#       #/")
  #print( "/ / / / / /")    

#Greatest number challenge
#num1=int(input("Input the first number: "))
#num2 = int(input("Input the second number: "))
#if num1>num2:
  #print("The largest number is ", num1)
#else:
 # print("The largest number is ", num2)

#Nitrate challenge
#nitrate=float(input("Enter the nitrate level between 1 and 50: "))
#if nitrate>10:
 # print("Dose 3ml")
#elif nitrate>2.5:
 # print("Dose 2ml")
#elif nitrate>1:
 # print("Dose 1ml")
#else:
  #print("Dose 0.5ml")

#Portfolio grade challenge
#analysis = int(input("input how much you got in analysis section: "))
#design = int(input("input how much you got in design section: "))
#implementation = int(input("input how much you got in the implementation section: "))
#evaluation = int(input("input how much you got in the evaluation section: "))
#total_mark=evaluation +implementation+design+analysis
#print("You scored ", total_mark)
#if total_mark<4:
  #print("Your grade is U")
 # print("You were",4-total_mark,"marks away from the next grade")  
#elif total_mark>=4 and total_mark<13:
  #print("Your grade is G")
 # print("You were",13-total_mark,"marks away from the next grade")  
#elif total_mark>=13 and total_mark<22:
  #print("Your grade is F")
 # print("You were",22-total_mark,"marks away from the next grade")  
#elif total_mark>=22 and total_mark<31:
  #print("Your grade is E")
 # print("You were",31-total_mark,"marks away from the next grade")  
#elif total_mark>=31 and total_mark<41:
  #print("Your grade is D")
 # print("You were",41-total_mark,"marks away from the next grade")  
#elif total_mark>=41 and total_mark<54:
  #print("Your grade is C")
 # print("You were",54-total_mark,"marks away from the next grade")  
#elif total_mark>=54 and total_mark<67:
  #print("Your grade is B")
 # print("You were",67-total_mark,"marks away from the next grade")  
#elif total_mark>=67 and total_mark<80:
  #print("Your grade is A")
 # print("You were",80-total_mark,"marks away from the next grade")  
#elif total_mark>=80:
  #print("Your grade is A*")

#Periodic table challenge
#element=input("Enter the name of an element: ")

#if element == "Sodium":
 # print("Element:Sodium")
 # print("Atomic mass:23")
 # print("Group:Alkali metals")
  
#if element == "Potassium":
 # print("Element: Potassium")
 # print("Atomic mass: 39")
 # print("Group: Alkali metals")

#if element == "Rubidium":
 # print("Element: Rubidium")
 # print("Atomic mass: 85")
 # print("Group:Alkali metals")

#if element == "Beryllium":
 # print("Element: Beryllium")
 # print("Atomic Mass: 9")
 # print("Group: Alkaline earth metals")

#if element ==  "Magnesium":
 # print("Element: Magnesium")
 # print("Atomic mass: 24")
 # print("Group: Alkaline earth metals")

#if element == "Calcium":
  #print("Element: Calcium")
  #print("Atomic mass: 40")
  #print("Group: Alkaline earth metals")

#Train ticket challenge
#stations =int(input("Enter how many stations you will pass through: "))
#confused = stations*20
#adults = int(input("Enter how many adults there will be: "))
#children= int(input("enter how many children there will be: "))
#time= int(input("Enter at what time your joureny wil begin: "))
#if time == 6 or time == 7 or time == 8 or time ==9:
 # confused = stations * 25
#cost = adults * confused
#cost = cost+ children * confused/2
#print("Your cost will be: ",cost)

#Hours worked challenge
#hours =int(input("enter how many hours you worked this week: "))
#hourly_wage=int(input("enter how much you get paid per hour: "))
#if hours >40 and hours <60:
  #overtime=hours-40
  #overtime_wage=overtime *(hourly_wage*1.5)
  #wage =(40*hourly_wage)+overtime_wage
 # print("Your salary is",wage)
#elif hours<=40:
  #print("Your salary is ",hours * hourly_wage)
  
  

  
