import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]
alphabet_udemy = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#since the Udemy solution does not use modulo to shift the edge cases, this is their solution...doubling the list. I dont like this solution


def encrypt(text, shift):
    message = []
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            ascii_num = ord(char.lower())  # Convert to lowercase for consistent handling
            shifted_num = (ascii_num - ord('a') + shift) % 26  # Adjust starting position to 'a'
            new_char = chr(shifted_num + ord('A' if is_upper else 'a'))
            message.append(new_char)
        else:
            message.append(char)

    return ''.join(message)

def decrypt(text, shift):
    # To decrypt, use the encrypt function with a negative shift
    return encrypt(text, -shift)

##Here is the enycrypt solution from Udemy. I thought it was interesting how different this was from my solution...
# I started programming in C++ and instantly disected this problem as an ASCII code shift...instead of using lists.
def encrypt2(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet_udemy.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet_udemy[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")


print(art.logo)
print("Welcome to Bayden Willms' Caesar Cipher.")
print("Send encrypted messages to your friends!")
text = input("Type your message:\n> ").lower()
shift = int(input("Type the shift number:\n"))
message = encrypt(text, shift)
print(f"Your encrypted message: {message}")

decrypted = decrypt(message, shift)
print(f"Here is the decrypted message: {decrypted}")


