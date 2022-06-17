import os
guess_word = input("Enter your word to be guessed: \n")
guess_word_list=[]
for counter in guess_word:
  guess_word_list.append(counter)
os.system("clear")
print(f"The word has {len(guess_word)} letters")
guesses = []
correct_guesses=[]
guessed = False
lives=6
guess_number = 1
print(guess_word_list)
while guessed == False and lives>0:
  print(f"Guess {guess_number}")
  try:
    while True:
      guess=input("Enter your letter guess: \n")
      break
  except:
    print("Invalid data")
  guesses.append(guess)
  if guess in guess_word_list:
    print("Correct")
  else:
    print("Incorrect")
    lives -=1
    print(f"You have {lives} lives left")
    
  correct_guesses.append(guess)
  i=0  
  for letter in guess_word_list:
    for correct in correct_guesses:
      if letter == correct:
        i+=1
  if i >=len(guess_word_list):
    guessed=True
  print (correct_guesses) 
  guess_number+=1