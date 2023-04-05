word_dict = {}

# Ask user for word and its description
# it shoud loop until he said to stop
while True:
    word = input("Give a word: ")
    description = input("Give a description for that word: ")
    word_dict[word] = description
    
    end = input("Do you want to stop the loop(y/n): ").lower()
    if end == "y":
        break

print("Dictionary: ")
for word, description in word_dict.items():
    print("{}: {}".format(word, description))