def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list
    with open(filename, 'r') as f:
        for line in f:
            #The line below appends the processed line to the list
            #the strip() removes the whitelines at the end of the line
            #the split(',') converts the string to a list and takes the first index
            cast_list.append(line.strip().split(',')[0])

    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)
