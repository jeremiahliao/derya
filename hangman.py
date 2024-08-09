import random

wordbank = ["philosophy", "cucumber", "amazon", "computer", "science"]
GUESS_LIMIT = 6

def run():
	res = input("Hello, welcome to Hangman! Press S to Start: ")
	if(res.lower() != 's'):
		print("Error!")
		return

	answer = random.choice(wordbank)
	output = ['_'] * len(answer)
	letterBank = []

	guess_count = 0
	num = 0

	print(output)
	while(guess_count < GUESS_LIMIT and num < len(answer)):
		res = input("Guess a letter: ")
		while(res in letterBank):
			res = input("Guess a letter: ")

		if(type(res) != str):
			print("Error")
			return

		i = 0							# initialize pointer
		cnt = 0							# initialize letter count
		while(i < len(answer)):			# loop through word
			cur = answer[i]				# initialize current letter
			
			if cur == res:
				output[i] = res
				cnt += 1
			i += 1

		if(cnt == 0):					# cnt will be 0 if letter isn't in word
			print("Wrong!")
			print()
			guess_count += 1
		else:
			print("Correct!")
			print()
			num += cnt

		letterBank.append(res)
		print(output)
		print("Letter Bank: ", letterBank)
		print()


	if(guess_count == GUESS_LIMIT):		# if guess limit is reached, player loses
		# max guesses reached
		print("You Lose!")
		print("The correct word was", answer)
	else:
		print("You win!")

	print()


# run program
run()