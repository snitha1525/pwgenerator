import random
import string

def generate_password(length=12, use_special_chars=True):
    
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation

   
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    print("Welcome to the Password Generator!")
    while True:
        try:
            length_input = input("Enter the length of the password (minimum 8, default is 12): ") or "12"
            length = int(length_input)
            if length < 8:
                print("Please enter a length of at least 8.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    use_special_chars = input("Include special characters? (y/n, default is y): ").strip().lower() != 'n'
    password = generate_password(length, use_special_chars)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
