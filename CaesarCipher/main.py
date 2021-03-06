from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
response = "yes"
print(logo)


def caesar(input_text, input_shift, input_direction):
    """Performs the Caesar Cipher algorithm for encryption and decryption"""
    result_text = ""
    for character in input_text:
        if character not in alphabet:
            result_text += character
        else:
            index = alphabet.index(character)
            if input_direction == "encode":
                result_text += alphabet[index - input_shift]
            elif input_direction == "decode":
                new_index = (index + input_shift) % 26
                result_text += alphabet[new_index]
    print(f"The {input_direction}d text is: {result_text}")


def main_menu():
    """Displays the main menu"""
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 26
    caesar(text, shift, direction)


while response == "yes":
    main_menu()
    response = input("Type 'yes' if you want to go aengain. Otherwise type 'no'.\n")

print("Goodbye")
