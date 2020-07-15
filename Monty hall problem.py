from random import seed
from random import random
import math
seed(77)

win_stick = 0
win_switch = 0
lose = 0

for _ in range(1000):
  prize = ["goat", "goat", "goat"]

  value = math.floor(random()*3)
  
  prize[value] = "car"

  mychoice = 0 # my initial choice always as the first one
  switched = False

  if prize[1] == "goat": # taking one goat out
    del prize[1:2]
  elif prize[2] == "goat":
    del prize[2:]
  
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

print(win_stick) #result : 155
print(win_switch) #result : 309
print(lose) #result: 536

# This means that swithching is roughly 2 times better than sticking with the initial choice.
# The chances of you losing versus winning is still 50:50.
# So I can conclude that with the possibility of you both switching and sticking, you have 50% of winning.
# However if you just choose to switch, the possibility goes up to 60%.