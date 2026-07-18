import math
import random as r

#print(math.sqrt(25))
#print(math.sin(30))
#print(math.pi)

rand=r.random(1,100)

while(True):
    guess=int(input("Enter the random number:"))

    if(rand==guess):
      print('You guess right ..7 cror ')
    if(rand>guess):
      print('You guess wrong number is greater than your soch ')
    if(rand<guess):
      print('You guess wrong number is less than your soch ')

