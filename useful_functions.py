def mean(num_list):
    return sum(num_list)/len(num_list)

def add_five(num_list):
    return [n + 5 for n in num_list]

def main(): #Alternative way of keeping the executables
    print("\nFROM THE MAIN() FUNCTION\n")
    print("Testing mean function")
    n_list = [34, 44, 23, 46, 12, 24]
    correct_mean = 30.5
    assert(mean(n_list) == correct_mean)

    print("Testing add_five function")
    correct_list = [39, 49, 28, 51, 17, 29]
    assert(add_five(n_list) == correct_list)

    print("All tests passed!")
#Assuming useful functions has some executable codes
#You can limit the execution by using a if __name__ conditional
#Alternatively include then in a functon called main() and call it in the if __name__ block

if __name__ == '__main__':
    print("Testing mean function")
    n_list = [34, 44, 23, 46, 12, 24]
    correct_mean = 30.5
    assert(mean(n_list) == correct_mean)

    print("Testing add_five function")
    correct_list = [39, 49, 28, 51, 17, 29]
    assert(add_five(n_list) == correct_list)

    print("All tests passed!")

#Alternatively
if __name__ == '__main__':
    main()
