def is_palindrome(s):
    
    s = s.replace(" ", "").lower()
    return s == s[::-1]


text = input("Enter a string: ")

if is_palindrome(text):
    print("Yes, it is a Palindrome.")
else:
    print("No, it is not a Palindrome.")
