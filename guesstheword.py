import random
# library that we use in order to choose
# on random words from a list of words

name = input("What is your name? ")

# Here the user is asked to enter the name first

print("Good Luck ! ", name)

words = ['rainbow', 'computer', 'science', 'programming',
		'python', 'mathematics', 'player', 'condition',
		'reverse', 'water', 'board', 'geeks','software','compact','laptop']
word = random.choice(words)
print("Guess the characters")
guesses = ''
turns = 10
while turns > 0:
	failed = 0
	for char in word:

		# comparing that character with
		# the character in guesses
		if char in guesses:
			print(char, end=" ")

		else:
			print("_")

			# for every failure 1 will be
			# incremented in failure
			failed += 1

	if failed == 0:
		# user will win the game if failure is 0
		# and 'You Win' will be given as output
		print("You Win\n")

		# this print the correct word
		print("\nThe word is: ", word)
		break

	# if user has input the wrong alphabet then
	# it will ask user to enter another alphabet
	print()
	guess = input("guess a character:")

	# every input character will be stored in guesses
	guesses += guess

	# check input with the character in word
	if guess not in word:
		turns -= 1
		print("Wrong\n")
		print("\nYou have", + turns, 'more guesses')

		if turns == 0:
			print("You Loose\n")
