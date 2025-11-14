from random import randint

n = randint(1,50)
a =0
guesses = 0
while (a != n):
    guesses+=1
    a = int(input("Guess the number: "))
    if (a>n):
        print("Lower number please")
    elif (a<n):
        print("Higher number please")

print(f"You have correctly guessed the number {n} in {guesses} attempts")
