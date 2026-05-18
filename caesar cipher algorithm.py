def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():
            # Determine uppercase or lowercase
            base = ord('A') if char.isupper() else ord('a')

            # Encrypt or decrypt
            if mode == "encrypt":
                new_char = chr((ord(char) - base + shift) % 26 + base)
            elif mode == "decrypt":
                new_char = chr((ord(char) - base - shift) % 26 + base)

            result += new_char
        else:
            # Keep spaces and symbols unchanged
            result += char

    return result


# User Input
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

# Encryption
encrypted_text = caesar_cipher(message, shift, "encrypt")
print("Encrypted Text:", encrypted_text)

# Decryption
decrypted_text = caesar_cipher(encrypted_text, shift, "decrypt")
print("Decrypted Text:", decrypted_text)