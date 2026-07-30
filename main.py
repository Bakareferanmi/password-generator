import random
import string

print("=" * 40)
print("      PASSWORD GENERATOR PRO")
print("=" * 40)

try:
    length = int(input("Password length: "))

    if length < 8:
        print("Password must be at least 8 characters.")
        exit()

    use_upper = input("Include uppercase? (y/n): ").lower() == "y"
    use_lower = input("Include lowercase? (y/n): ").lower() == "y"
    use_numbers = input("Include numbers? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"

    selected = []
    password = []

    if use_upper:
        selected.append(string.ascii_uppercase)
        password.append(random.choice(string.ascii_uppercase))

    if use_lower:
        selected.append(string.ascii_lowercase)
        password.append(random.choice(string.ascii_lowercase))

    if use_numbers:
        selected.append(string.digits)
        password.append(random.choice(string.digits))

    if use_symbols:
        selected.append(string.punctuation)
        password.append(random.choice(string.punctuation))

    if not selected:
        print("You must choose at least one option.")
        exit()

    all_characters = "".join(selected)

    while len(password) < length:
        password.append(random.choice(all_characters))

    random.shuffle(password)

    final_password = "".join(password)

    print("\nGenerated Password")
    print("-" * 30)
    print(final_password)

except ValueError:
    print("Please enter a valid number.")
