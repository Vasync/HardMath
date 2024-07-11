#!/usr/bin/python3
import random

chooseMin = input("Input min int for math: ");
chooseMax = input("Input max int fpr math: ");

quest = random.randint(chooseMin, chooseMax) * random.randint(chooseMin, chooseMax) / random.randint(chooseMin, chooseMax) + random.randint(chooseMin, chooseMax) + random.randint(chooseMin, chooseMax) - random.randint(chooseMin, chooseMax)

print("MATH: ", quest)

kq = input("The result is ")
if isinstance(kq, int) :
  if kq == quest:
    echo("Oh my God, you have successfully solved a difficult problem!")
  else:
    echo("Too bad you answered wrong, try again next time!") 
else:
  echo("The result must be an integer") 
  
