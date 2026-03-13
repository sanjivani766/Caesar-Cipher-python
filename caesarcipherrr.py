import string

ALPHABET = string.ascii_letters


def encrypt(text, shift):
    """Encrypt text using Caesar Cipher."""
    encrypted = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char

    return encrypted


def decrypt(text, shift):
    """Decrypt text using Caesar Cipher."""
    return encrypt(text, -shift)


def get_shift():
    """Get valid shift value from user."""
    while True:
        try:
            shift = int(input("Enter shift value (0-25): "))
            if 0 <= shift <= 25:
                return shift
            else:
                print("Shift must be between 0 and 25.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("\n===== Caesar Cipher Security Tool =====\n")

    while True:
        print("Choose an option:")
        print("1. Encrypt Message")
        print("2. Decrypt Message")
        print("3. Exit")

        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            message = input("\nEnter message to encrypt: ")
            shift = get_shift()
            encrypted = encrypt(message, shift)
            print("\nEncrypted Message:", encrypted, "\n")

        elif choice == "2":
            message = input("\nEnter message to decrypt: ")
            shift = get_shift()
            decrypted = decrypt(message, shift)
            print("\nDecrypted Message:", decrypted, "\n")

        elif choice == "3":
            print("\nExiting program. Goodbye!")
            break

        else:
            print("\nInvalid option. Please try again.\n")


if __name__ == "__main__":
    main()