import random

print("=" * 35)
print("   🎮 THE SECRET NUMBER GAME")
print("=" * 35)

name = input("What is your name, player? ")
print(f"\nWelcome, {name}! 😈")

secret_number = random.randint(1, 20)
attempts = 5
score = 100

print("\nI'm thinking of a number between 1 and 20.")
print("You have 5 attempts to guess it!")

while attempts > 0:
    try:
        guess = int(input("\nEnter your guess: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if guess < 1 or guess > 20:
        print("Choose a number between 1 and 20!")
        continue

    if guess == secret_number:
        print("\n🎉 YOU WON!!!")
        print(f"You cracked the code, {name}!")
        print(f"Your final score is {score} points!")
        break

    elif guess < secret_number:
        print("Too LOW! 📉")
    else:
        print("Too HIGH! 📈")

    attempts -= 1
    score -= 20

    if attempts > 0:
        print(f"❤️ Attempts remaining: {attempts}")

if attempts == 0:
    print("\n💀 GAME OVER!")
    print(f"The secret number was {secret_number}.")
    print("Better luck next time!")

print("\nThanks for playing! 👋")