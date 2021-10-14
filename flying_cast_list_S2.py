def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list
    with open(filename, 'r') as f:
        cast_list = f.readline()
        #This approach does not work because the entire line is converted to a
        #list element. It is more difficult to process each element of the line.
        #The best approach is to process each line before it is converted to a
        #list element
        #cast_list.append(line.strip().split(',')[0])

    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)
