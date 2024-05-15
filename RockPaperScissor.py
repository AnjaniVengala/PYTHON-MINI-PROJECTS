import random

print("\n\n\n\n\t\t\t\tEnter s for STONE, p for PAPER and z for SCISSOR\n\t\t\t\t\t\t\t")
you = input().lower()

n = random.randint(0, 99)
if n < 33:
    computer = 's'
elif n < 66:
    computer = 'p'
else:
    computer = 'z'

if you == computer:
    result = -1
elif (you == 's' and computer == 'p') or (you == 'p' and computer == 'z') or (you == 'z' and computer == 's'):
    result = 0
else:
    result = 1

if result == -1:
    print("\n\n\t\t\t\tGame Draw!\n")
elif result == 1:
    print("\n\n\t\t\t\tWow! You have won the game!\n")
else:
    print("\n\n\t\t\t\tOh! You have lost the game!\n")

print(f"\t\t\t\tYou chose : {you} and Computer chose : {computer}")
