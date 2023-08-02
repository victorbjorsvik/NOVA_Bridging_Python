def even_index(text):
    new_text = text[0:len(text): 2]
    return new_text

def even_index2(text):
    new_text = ""
    for letter in text[0:len(text):2]:
        new_text += letter
    return new_text

print(even_index2("Python"))
print(even_index("Inception"))
print(even_index("Owowowowowow"))