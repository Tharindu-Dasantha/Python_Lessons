# First lets take a input of string type
string = "Hello there!"
# now lets print the sting and the string with the center method
print(string)
# Center is a string method that work same as the center align in ms word
# in center you need to input a amount of int inside the brackets 
# Then python will create a string in that length long and paste the string in 
# the middle of the second autocreated string
# And it fill up the rest with just blank spaces
print(string.center(20))

# But what if you enter a value lower than the length of the given stirng
print(string.center(5))
# As you can see the it just ignore the center method and print out the sting it self