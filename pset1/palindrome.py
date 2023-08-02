def is_palindrome(text):
    text = text.replace(" ","").lower()
    if len(text) <= 1:
        return True
    else:
        return text[0] == text[-1] and is_palindrome(text[1:-1])

def is_pal(text):
    text = text.lower().replace(" ","")
    reversed = ""
    for letter in text:
        reversed = letter + reversed
    return reversed == text

    
print(is_palindrome("abba"))
print(is_palindrome("racecar"))
print(is_palindrome("gods"))
print(is_palindrome("Intro to Programming"))
print(is_palindrome("Was it a cat I saw"))

print(is_pal("abba"))
print(is_pal("racecar"))
print(is_pal("gods"))
print(is_pal("Intro to Programming"))
print(is_pal("Was it a cat I saw"))