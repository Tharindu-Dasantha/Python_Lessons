numbers_list = [1,2,"a",3]

for number in numbers_list:
    try:
        numbers_list.append(int(number))
    except ValueError:
        print(f"Error: {number} is not a valid integer")