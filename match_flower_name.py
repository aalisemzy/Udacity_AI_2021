# Write your code here
def flowers1(flowers_file):
    flowers_dict ={}
    flowers_list = []
    flower_key = []
    flower_value = []
    with open(flowers_file) as f:
        for line in f:
            flower_key.append(line.strip().split(':')[0].lstrip().rstrip())
            flower_value.append(line.strip().split(':')[1].lstrip().rstrip())
        for fkey, fvalue in zip(flower_key, flower_value):
            flowers_dict[fkey] = fvalue
    return flowers_dict

def flowers2(flowers_file):
    flowers_dict ={}
    with open(flowers_file) as f:
        for line in f:
            flowers_dict[line.strip().split(':')[0].lstrip().rstrip()] = line.strip().split(':')[1].lstrip().rstrip()
    return flowers_dict
def main():
    flowerName = flowers1('flowers.txt')
    userName = input("Enter your First [space] Last name only: ").title()
    userLetter = userName[0]

    if userLetter.isalpha():
        print("Unique flower name with {} letter: {}".format(userLetter, flowerName[userLetter]))
    else:
        print("{} is not a letter. Enter a proper name next time!".format(userLetter))


if __name__ == '__main__':
    main()
# HINT: create a dictionary from flowers.txt

# HINT: create a function to ask for user's first and last name


# print the desired output
