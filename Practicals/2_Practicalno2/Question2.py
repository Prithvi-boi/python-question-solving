'''
AIM: 
- To analyse a provided string. 
    1 - Count vowels in your text. 
    2 - Reverse the text using slicing. 
    3 - Check if the text is palindrome. 
    4 - Convert your text to upper lower and title case.
'''


while True:
    # Taking a Text from the user
    text = input("Enter Text: ").lower(); print('\n')

    # 4 - options
    print(''' Select Operation You want to do
          1 - Count vowels in your text. 
          2 - Reverse the text using slicing. 
          3 - Check if the text is palindrome. 
          4 - Convert your text to upper lower and title case. \n '''
        )
    
    # Selecting option
    for max_attempt in range(1,5,1):
        option = int(input("Select Option(1-4): "))

        if option == 1 or option == 2 or option == 3 or option == 4:

            # counting vowels
            if option == 1:
                vowels = ["a","e","i","o","u"]
                vowels_count = 0
                for i in text:
                    for j in vowels:
                        if i == j:
                            vowels_count += 1
                print(f'There are {vowels_count} vowels in your text \n')
                continue
                
            # Reversing the text using slicing.
            elif option == 2:
                print('Reversed text using slicing: ',text[::-1],' \n') 
                continue

            # palindrom checker
            elif option == 3:
                reversed_text = text[::-1]
                if text == reversed_text:
                    print(f'Yes, it is a palindrome : {text}  \n')
                else:
                    print(f'No, it is not a palindrome : {text}  \n')
                continue
                
            # Case Converter
            elif option == 4:
                print("Case Coversion of your text:\n"\
                    "upper():",text.upper(),'\n'\
                    "lower():",text.lower(),'\n'\
                    "title():",text.title(),'\n','\n'\
                    )
                continue

        else:
            print(f"There is no option for: '{option}' attempts: {max_attempt}/4 , Try again \n")

    

        # Checking if the user want to check again
    restart_check = input("Want to check with different TEXT? (yes/no):").lower()

    if restart_check == "yes":
        print('Okhay')
    elif restart_check == "no":
        print('Ok Bye')
        break
    else:
        print("Type YES/NO only")