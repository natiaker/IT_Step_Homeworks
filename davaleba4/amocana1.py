text = str(input("შეიყვანეთ ტექსტი: ")).lower()
reversed_text = text[::-1]
isPalindrome = text == reversed_text

if isPalindrome:
    print("შეყვანილი ტექსტი არის პალინდრომი")
else:
    print("შეყვანილი ტექსტი არ არის პალინდრომი")
