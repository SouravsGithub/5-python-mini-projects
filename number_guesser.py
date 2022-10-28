import random

random_number = random.randint(0,20)
print(random_number)
guess = 1
guessed_number = input("Choose a random number between 0 and 20: ")
if guessed_number.isdigit():
  guessed_number = int(guessed_number)
else:
  print("Please enter a valid number next time.")
  quit()

while random_number != guessed_number:
  if guessed_number > random_number:
    guessed_number = input("Too high, choose another one: ")
    if guessed_number.isdigit():
      guessed_number = int(guessed_number)
    else:
      print("Please enter a valid number next time.")
      quit()
    guess += 1
  else:
    guessed_number = input("Too low, choose another one: ")
    if guessed_number.isdigit():
      guessed_number = int(guessed_number)
    else:
      print("Please enter a valid number next time.")
      quit()
    guess += 1

print("It took you " + str(guess) + " guesses to get the correct answer.")