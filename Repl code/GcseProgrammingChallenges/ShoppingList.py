print("Type clear to clear the list \nType print to print the list\nor just type item to enter")
shopping_list=[]
while True:
  choice=input("Input: ")
  if choice == "clear":
    print("List cleared")
    shopping_list = []
  elif choice == "print":
    for counter in shopping_list:
      print(counter)
  else:
    shopping_list.append(choice)