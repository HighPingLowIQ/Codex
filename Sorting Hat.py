# Write code below 💖
import time
import random
import math

print("Today I choose what house you are in.")
time.sleep(2) 
print("Let's begin.")
print("")

gryffindor_points = 0
ravenclaw_points = 0
hufflepuff_points = 0
slytherin_points = 0

house_points = {
    "Gryffindor": gryffindor_points,
    "Ravenclaw": ravenclaw_points,
    "Hufflepuff": hufflepuff_points,
    "Slytherin": slytherin_points
}

dawn_question = float(input("Do you like more Dawn or Dusk (1-2)?: "))

if dawn_question == 1:
  print("Hmm let me think...")
  time.sleep(1)
  print("One point to Gryffindor and Ravenclaw!!")
  gryffindor_points += 1
  ravenclaw_points += 1
  print("")
elif dawn_question == 2:
  print("Hmm let me think...")
  time.sleep(1)
  print("One point to Hufflepuff and Slytherin!!")
  hufflepuff_points += 1
  slytherin_points += 1
else:
  print("Wrong input")

print("")
time.sleep(2)
print("Alright, next question")
time.sleep(1)

print("Which one of these would you want people to remember you as?")
print("1: The Good")
print("2: The Great")
print("3: The Wise")
print("4: The Bold")
dead = float(input("Please answer with a 1-4: "))

if dead == 1:
  hufflepuff_points += 2
  time.sleep(1)
  print("2 points to Hufflepuff!")
elif dead == 2:
  slytherin_points += 2
  time.sleep(1)
  print("2 points to Slytherin!")
elif dead == 3:
  ravenclaw_points += 2
  time.sleep(1)
  print("2 points to Ravenclaw!")
elif dead == 4:
  gryffindor_points += 2
  time.sleep(1)
  print("2 points to Griffindor!")
else:
  print("Worng input.")

time.sleep(1)
print("")
print("Let's move on to the last question.")
print("")
time.sleep(2)

print("Which instrument pleases you the most?")
print("1: The Violin")
print("2: The Trumpet")
print("3: The Piano")
print("4: The Drum")
instrument = float(input("Please answer with a 1-4: "))

if instrument == 1:
  slytherin_points += 4
  time.sleep(1)
  print("4 points to Slytherin!")
elif instrument == 2:
  hufflepuff_points += 4
  time.sleep(1)
  print("4 points to Hufflepuff!")
elif instrument == 3:
  ravenclaw_points += 4
  time.sleep(1)
  print("4 points to Ravenclaw!")
elif instrument == 4:
  gryffindor_points += 4
  time.sleep(1)
  print("4 points to Griffindor!")
else:
  print("Wrong input.")

time.sleep(3)
print("")
print("Now I will tell you what house you are in...")

num = random.randint(1, 4)
print("")

if num == 1:
  print("You are in Griffindor!")
elif num == 2:
  print("You are in Slytherin!")
elif num == 3:
  print("You are in Hufflpuff!")
elif num == 4:
  print("You are in Ravenclaw!")
else:
  print("You aren't worthy of house or being here at Hogwarts")

time.sleep(2)
print("")

sorted_houses = sorted(house_points.items(), key=lambda x: x[1], reverse=True)
for house, points in sorted_houses:
    print(f"{house}: {points}")

print("Thank you for coming to Howarts")
time.sleep(4)
