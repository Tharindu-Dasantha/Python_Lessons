# Casefold is a method of string which used like this:
string = "Hello, my name is Tharindu"
string.casefold()

# This is similar to the lower() method of a string. But more strong
# What does that means well lets test it out
# first lets make a string type variable
sentence = "He was reading a BOOK at that time."
# now we print out the sentence in useing lower and the casefold
print(sentence.lower())
print(sentence.casefold())
# you can see both are the same 

# But now let's use a letters in other language which is not english but has capital and simple 
# letters as a example im using Greek
letters = "ΓΔΠΣΦΨΩ"
# now lets try and use those two methods (this is useless step but i only add this to answer the question of
# what will happen if we use them on capital greek letters)
print(letters.lower())
print(letters.casefold())
# You can see those are also the same but what if the greek letter is already 
simpleletters ="ßå"
# now lets do the same thing
print(simpleletters.lower())
print(simpleletters.casefold())