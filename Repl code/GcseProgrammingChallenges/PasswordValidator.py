cPassword=False
while cPassword == False:
  password=input("Enter your password: \n")
  uppercase=False
  lowercase=False
  for counter in password:
    if counter.isupper():
      uppercase=True
    if counter.islower():
      lowercase=True
  if uppercase == True and lowercase == True:
    if len(password)>7:
      cPassword=True
