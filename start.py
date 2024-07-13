import random

# Function to validate if input can be converted to integer
def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# Get user inputs and convert them to integers
chooseMin = int(input("Input min int for math: "))
chooseMax = int(input("Input max int for math: "))

# Generate the math problem
a = random.randint(chooseMin, chooseMax)
b = random.randint(chooseMin, chooseMax)
c = random.randint(chooseMin, chooseMax)
d = random.randint(chooseMin, chooseMax)
e = random.randint(chooseMin, chooseMax)

quest_str = a,' × ',b,' ÷ ',c,' + ',d,' + ',e
quest = a * b / c + d + e

print("MATH: ", quest_str)

# Get user's answer and validate if it's an integer
kq = input("The result is: ")
if is_integer(kq):
    kq = int(kq)  # Convert kq to integer
    # Check if the answer is correct
    if kq == quest:
        print("Oh my God, you have successfully solved a difficult problem!")
    else:
        print("Too bad you answered wrong, try again next time!")
else:
    print("The result must be an integer")
