# When first seeing count method in string many people think its for counting the length of the string
# But thats not the case count take 3 arguments (inputs inside the braket) 
# first it takes a stirng type value
# secondly it takes int type value (optional)
# thirdly it takes int type value(optional)
# What count method do is it look at the stirng(main string) and go to the place where the second int is indexd at if there is no second element then it starts from the beginning
# and then it looks at the third element and save it as the end point if not given it take the end of the string as the end point
# Finally it looks for the given string( value given to the method) in that range and print out how many times it has repeted
string = "happy wife happy life"
print(string)
print(string.count("happy"))