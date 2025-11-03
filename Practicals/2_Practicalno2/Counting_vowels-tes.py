
text = input("Enter Text: ").lower(); print('\n')

vowels = ["a","e","i","o","u"]

vowels_count = 0

for i in text:
    for j in vowels:
        if i == j:
            vowels_count += 1

print(vowels_count)