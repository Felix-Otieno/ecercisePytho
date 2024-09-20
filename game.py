import random
score = 10
randomNumber = random.randint(1,10)
while True:
    userNumberInput = int(input("Guess: "))
    if userNumberInput == randomNumber:
         print("Congratulations you guess it right! your score is", str(score))
         break
    else:
         print("Better luck next time") 
         score -= 1    