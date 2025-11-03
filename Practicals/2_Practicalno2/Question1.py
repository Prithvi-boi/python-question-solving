
text = "  Hello World my name is python    "
print("Text used:'",text,"'",'\n')

print("len() - Length of Text used:",len(text),'\n')

print(
    "-____________Slicing_____________",'\n'
    "text[4:12]   :", text[4:12]       ,'\n'
    "text[10:]    :", text[10:]        ,'\n'
    "text[-12:-1] :", text[-12:-1]     ,'\n'
    )

print(
    "-____________Case Conversions______",'\n'
    "upper()      :", text.upper()      ,'\n'
    "lower()      :", text.lower()      ,'\n'
    "title()      :", text.title()      ,'\n'
    "capitalize() :", text.capitalize() ,'\n'
    "swapcase()   :", text.swapcase()   ,'\n'
    )


print(
    "-____________ Find and Replace Methods______________",'\n'
    "replace()    :", text.replace('python','JavaScript') ,'\n'
    "index()      :", text.index("m")                     ,'\n'
    "find()       :", text.find('my')                     ,'\n'
    "count()      :", text.count('o')                     ,'\n'
    "startswith() :", text.startswith('H')                ,'\n'
    "endswith()   :", text.endswith('H')                  ,'\n'
    )

print(
    "-____________ Boolean String Methods_______",'\n'
    "isalpha()    :", text.isalpha()             ,'\n'
    "isdigit()    :", text.isdigit()             ,'\n'
    )


print(
    "-____________ Strip Methods________________",'\n'
    "Before strip() :", "'",  text        ,"'"   ,'\n'
    "After strip()  :", "'",  text.strip(),"'"   ,'\n'
    )

print(
    "____________ Split Methods__________________________",'\n'
    "split() - using '' as seperator :",text.split()      ,'\n'
    "split() - using 'o' as seperator :",text.split('o')  ,'\n'
    )

print(
    "____________ F-String_______________________________",'\n'
    f' This Text "{text}" is used for doing this practical','\n'
    )

print(
    "____________ Concatenation___________________________",'\n'
    "This Text " + text + "is used for doing this practical",'\n'
    )