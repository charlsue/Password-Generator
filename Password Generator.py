#Password Generator Project
while True:
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    print("\n")

    nr_letters= int(input(f"How many letters would you like in your password?\n"))
    for letter in letters:
        random_letter = random.sample(letters, nr_letters)  
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    for symbol in symbols:
        random_symbols = random.sample(symbols, nr_symbols)   
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    for number in numbers:
        random_numbers = random.sample(numbers, nr_numbers) 

    combined_lists = random_letter + random_numbers + random_symbols
    shuffled_lists = random.shuffle(combined_lists)
    joined_strings = "".join(combined_lists)
    print(joined_strings)
    print("\n")
    try_again = input("Would you like to try again? Y/N\n").lower()
    if try_again == "y":
        continue
    else:
        break