# inputs 
numbers = input("Enter a list of numbers separated by commas: ")
want = input("What do you want to so with the list: \n a-maximum Value \n b-minimum Value \n c-average Value \n").lower()

newlist = numbers.split(',')

# Convert the input into a list of ints
# for i in new:
#     j = type(int(i))
# one line for loop 
try:
    new = [int(i) for i in newlist]
except ValueError:
    print("Please only enter numbers.")
else:
    minvalue = min(new)
    maxvalue = max(new)

    # Average of the list
    total = sum(new)
    numOfElements = len(new)
    average = total // numOfElements

    match want:
        case 'a':
            print(maxvalue)
        case 'b':
            print(minvalue)
        case 'c':
            print(average)
        case _:
            print("Invalid input")