import random
import string

print("=" * 35)
print("   PASSWORD GENERATOR")
print("=" * 35)

try:
    length = int(input("Enter password length: "))

    if length < 4:
        print("Password length should be at least 4.")
        exit()

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = "".join(
        random.choice(characters)
        for _ in range(length)
    )

    print("\nGenerated Password:")
    print(password)

except ValueError:
    print("Please enter a valid number.")
