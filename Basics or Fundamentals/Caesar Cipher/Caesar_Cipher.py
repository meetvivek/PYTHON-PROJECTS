from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(plain_text, shift_amount, cipher_direction):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            if cipher_direction == "decode":
                position -= shift_amount
            else:
                position += shift_amount
            cipher_text += alphabet[position]
        else:
            cipher_text += char
    print(f"The {cipher_direction}d test is {cipher_text}")


print(logo)

should_end = False
while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    if (direction == "encode") or (direction == "decode"):
        text = input("Type your message: ").lower()
        shift = int(input("Type the shift number: "))
        shift %= 26

        caesar(plain_text=text, shift_amount=shift, cipher_direction=direction)

        restart = input("Type 'Yes' to continue or 'No' to exit: ").lower()
        if restart == "no":
            should_end = True
            print("Goodbye")

    else:
        print("Please enter valid direction. Try Again.")
