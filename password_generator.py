import secrets
import string


def generate_password(length, complexity="strong"):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    password_chars = []

    if complexity == "simple":
        alphabet = lowercase + uppercase
        password_chars.append(secrets.choice(lowercase))
        password_chars.append(secrets.choice(uppercase))

    elif complexity == "moderate":
        alphabet = lowercase + uppercase + digits
        password_chars.extend([
            secrets.choice(lowercase),
            secrets.choice(uppercase),
            secrets.choice(digits)
        ])

    elif complexity == "strong":
        alphabet = lowercase + uppercase + digits + symbols
        password_chars.extend([
            secrets.choice(lowercase),
            secrets.choice(uppercase),
            secrets.choice(digits),
            secrets.choice(symbols)
        ])

    else:
        raise ValueError("Invalid complexity level")

    while len(password_chars) < length:
        password_chars.append(secrets.choice(alphabet))

    secrets.SystemRandom().shuffle(password_chars)

    return ''.join(password_chars)


def main():
    print("===== PASSWORD GENERATOR =====")

    while True:
        try:
            length = int(input("Enter password length (minimum 4): "))
            if length >= 4:
                break
            print("Length must be at least 4.")
        except ValueError:
            print("Please enter a valid number.")

    print("\nComplexity Levels")
    print("1. Simple (Letters only)")
    print("2. Moderate (Letters + Digits)")
    print("3. Strong (Letters + Digits + Symbols)")

    while True:
        choice = input("Choose complexity (1-3): ")

        if choice == "1":
            complexity = "simple"
            break
        elif choice == "2":
            complexity = "moderate"
            break
        elif choice == "3":
            complexity = "strong"
            break
        else:
            print("Please enter 1, 2, or 3.")

    password = generate_password(length, complexity)

    print("\nGenerated Password:")
    print(password)


if __name__ == "__main__":
    main()