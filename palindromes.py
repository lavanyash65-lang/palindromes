import sys

if len(sys.argv) == 2:
    text = sys.argv[1]
    print("User provided input value:")
else:
    print("No input given - using default value:")
    text = "level"

if text == text[::-1]:
    print(f"'{text}' is a palindrome")
else:
    print(f"'{text}' is not a palindrome")
