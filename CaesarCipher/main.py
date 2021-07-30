alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_number):
    encrypted_text = ""
    for letter in plain_text:
        index = alphabet.index(letter)
        encrypted_text += alphabet[index - shift_number]
    return encrypted_text


def decrypt(plain_text, shift_number):
    decrypted_text = ""
    for letter in plain_text:
        index = alphabet.index(letter)
        decrypted_text += alphabet[index + shift_number]
    return decrypted_text


if direction == "encode":
    print("The encoded text is: " + encrypt(text, shift))
elif direction == "decode":
    print("The decoded text is: " + decrypt(text, shift))
else:
    print("Wrong input for direction")
