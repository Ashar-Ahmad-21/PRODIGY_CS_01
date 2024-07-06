def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - shift_amount - shift) % 26 + shift_amount)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def main():
    while True:
        choice = input("Type 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").lower()
        if choice == 'q':
            break
        if choice not in ['e', 'd']:
            print("Invalid choice, please try again.")
            continue

        message = input("Enter the message: ")
        shift = int(input("Enter the shift value: "))

        if choice == 'e':
            result = encrypt(message, shift)
            print(f"Encrypted message: {result}")
        elif choice == 'd':
            result = decrypt(message, shift)
            print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()
