#Quiz Password generator
#TODO: First import the `random` module

import random

# We begin with an empty `word_list`
word_file = "word_list.txt"
word_list = []

# We fill up the word_list from the `words.txt` file
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# TODO: Add your function generate_password below
# It should return a string consisting of three random words
# concatenated together without spaces
def generate_password():
    choice = [random.choice(word_list) for i in range(3)] #Using list comprehension to generate list
    choice_str =''
    for ele in choice:
        choice_str+=ele
    return choice_str
#   ALternatively to generate elemets

def generate_password_2():
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)

def generate_password_3():
    return ''.join(random.sample(word_list, 3))



# Now we test the function
print(generate_password())
