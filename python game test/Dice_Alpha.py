import random

player = random.randint(1,6)
ai = random.randint(1,6)

if player > ai :
    print("You Win") #notice indentation
else:
    print("You Lose")
