while True:
  email = input("Enter your email address: ")
  dot = False
  includes_at = False
  pre_at = False
  post_dot = False
  i=0
  for counter in email:
    if counter == "@":
      includes_at = True
      at_location=i
    if counter == ".":
      dot_location = i
      