square_amount = int(input("Enter how many numbers you want squared: \n"))
for counter in range(1,square_amount+1):
  square = counter*counter
  print(f"{counter} squared equals {square}")