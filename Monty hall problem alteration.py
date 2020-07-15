# Suppose we play a variation of the Monty Hall problem. The host of the game show forgot which
# door the car is behind. So after you pick your door, he opens one of the other doors at random. It may be
# that he accidentally shows you the door with the car. In that case, you lose (unfortunately). If he opens a
# door and shows you a goat, should you remain with your choice of doors? Or switch to the other unopened
# door? Prove your answer by showing the probability of winning in either case.

from random import seed
from random import random
import math
seed(100)

win_stick = 0
win_switch = 0
lose = 0

for _ in range(10000):
  prize = ["goat", "goat", "goat"]

  value = math.floor(random()*3)

  prize[value] = "car"

  mychoice = 0 # my initial choice always as the first one
  switched = False

  hostChoice = math.floor(random()*2) + 1

  if prize[hostChoice] == "car": # if host chooses car, lose
    lose += 1
  else:
    show = prize.pop(hostChoice) # if not, show the goat and continue
    choiceValue = math.floor(random()*2)
    
    if choiceValue == 0: # random choices of swtiching or not switching
      switched = False
    else:
      switched = True
      mychoice = 1

    if prize[mychoice] == "car" and switched == False:
      win_stick += 1
    elif prize[mychoice] == "car" and switched == True:
      win_switch += 1
    else:
      lose += 1

print(win_stick) #result : 1696
print(win_switch) #result : 1667
print(lose) #result: 6637

# In this case the probability of winning by sticking and switching is the same.
# The chances of losing is 2/3.