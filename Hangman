import random
import requests
from time import sleep

response = requests.get("https://random-word-api.herokuapp.com/word?number=10000")

if response.status_code == 200:
    words = response.json()
else:
    print("Failed to fetch", response.status_code)
    exit()

random_word = random.choice(words).lower()
length_random_word = len(random_word)

print()
print()
print("Welcome to Hangman!")
sleep(2)
print()
print("Let's begin!")
sleep(2)
print()
print("The length of your word is", length_random_word, "letters.")
sleep(2)
print()
print("You have up to 5 mistakes or you fail!")
print()

mistakes = 5
guesses = ""

while mistakes > 0:
    display = ""
    for char in random_word:
        if char in guesses:
            display += char + " "
        else:
            display += "_ "
    print("Word:", display)
    print()
    
    if "_" not in display:
        print("You win!")
        print("The word was", random_word)
        break
    
    guess = input("What is your guess?: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guesses:
        print("You already guessed that letter!")
        continue
    
    guesses += guess
    
    if guess in random_word:
        print("Good guess!")
    else:
        mistakes -= 1
        print("Wrong!")
        print("You have", mistakes, "more guesses.")
    
    print()
    
    if mistakes == 0:
        print("You lose!")
        print("The word was", random_word)
        break
