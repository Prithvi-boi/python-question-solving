'''
Palindrome 
'''
text = input('Enter Text: ').strip().lower()

reversed_text = text[::-1]

if reversed_text == text:
    print("It is a palindrome")
else:
    print("It is not a palindrome")