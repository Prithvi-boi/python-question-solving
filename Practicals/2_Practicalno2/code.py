text = input("Enter a string to analyze: ")
vowel_counts = {}
for v in vowel_counts:
 count_lower = text.count(v)
 count_upper = text.count(v.upper())
 vowel_counts[v] = count_lower + count_upper
reversed_text = text[::-1]
cleaned_text = text.replace(" ", "")
cleaned_text_lower = cleaned_text.lower()
reversed_cleaned = cleaned_text_lower[::-1]
is_palindrome = cleaned_text_lower == reversed_cleaned
upper_text = text.upper()
lower_text = text.lower()
title_text = text.title()
print(f"Original string: {text}")
print(f"Vowel occurrences: {vowel_counts}")
print(f"Reversed string: {reversed_text}")
print(f"Is palindrome?: {is_palindrome}")
print(f"Uppercase: {upper_text}")
print(f"Lowercase: {lower_text}")
print(f"Title case: {title_text}")
