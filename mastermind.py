import random
#Amogh Ganjikunta
#AP CSP
numbers = []
for i in range(4):
  num = int(random.randrange(1,9))
  numbers.append(num)
guesses = []
var = 1
for i in range(4):
  guess = input(f"enter number {var} of your guess:")
  guesses.append(guess)
  var = var + 1
correct = False
i = 1
tries = 0
while correct == False:
  correctnum = 0
  for it in range(4):
    if guesses[i] == numbers[i]:
      correctnum = correctnum + 1
      i = i + 1
  if correctnum == 4:
    correct = True
  print((f"you got {correctnum} numbers correct"))
  var1 = 1
  guesses1 = []
  for i in range(4):
   guesss = input(f"enter number {var1} of your guess:")
   guesses1.append(guesss)
   var1 = var1 + 1
print("You guessed the number after" + tries + "tries")


