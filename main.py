import random
from enum import nonmember, member

options=("rock","paper","scissors")
player=None
comp=random.choice(options)
while player not in options:
    player=input("choose rock, paper, or scissors: ")

print(f"i choosed {comp}")
if player==comp:
    print("its a tie!")
elif player=="rock" and comp=="scissors":
    print("ahh u win!")
elif player=="paper" and comp=="rock":
    print("ahh u win!")
elif player=="scissors" and comp=="paper":
    print("ahh u win!")
else:
    print("HAHA u lost!")
