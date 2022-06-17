multiplier = int(input("Enter the number you want multiplied: \n"))
for counter in range(1,101):
  answer = counter*multiplier
  print(f"{counter}*{multiplier}={answer}")