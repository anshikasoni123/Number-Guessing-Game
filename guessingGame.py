import random
print("Number Guessing Game")
number = random.randint(1,9)
chances = 0
print("Guess a number (between 1 and 9)")

while chances < 5:
    guess = int(input("Enter your guess :- "))

if guess == number:
    print("Congratulations!! You Won")
elif guess < number:
    print("too low ! guess the higher number than",guess)    
else:
    print("too high ! guess the lower number than",guess)          

chances += 1

if not chances < 5:
    print("You lose! The number is", number) 