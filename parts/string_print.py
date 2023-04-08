# Lets say we have string like this 
newString = "Hello world! My name is Tharindu Edirisinghe."

# to print a letter inside a stirng we can use couple of methods
# First if we know where the letter is in the string we can use index to print the letter
print(newString[1] , newString[6]) # Like this 

# secondly we can take the index of a letter if we know the letter like this
indexOfLetter = newString.index("M")
print(indexOfLetter)

# we can also break a string into parts using this format
print(newString[1:5]) # first number is the staring point and secong number is the end point
print(newString[:5]) # If you want to start from the beginning
print(newString[5:]) # If you want to print every thing from a place to the end