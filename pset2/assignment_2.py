phone_book = {
    'James':218989111, 
    'Helen':910110000, 
    'Mary':910087856, 
    'Sam':900034234, 
    'Jack':219009000
}


def add_contact(name, phone):
    # Data validation
    if name in phone_book:
        return False
    # If not yet added -> insert into phone book
    else:
        phone_book[name] = phone
    return True


def find_phone(name):
    # Data validation
    if name in phone_book:
        # Return if found
        return phone_book[name]
    # Else (not found) -> return None
    else:
        return None


def sum_all(number):
    # Establish list
    l = []
    # Get numbers in range
    for i in range(1, number + 1):
        l.append(i)
    
    # Get sum of items in list
    sigma = sum(l)
    
    return l, sigma



"""
Test your functions here
You must comment your tests when submiting your work
"""

print(add_contact("Bruce",912345)) #True
print(add_contact("James",901242)) #False 

print(find_phone("Thomas")) #None
print(find_phone("Jack")) #219009000

print(sum_all(3)) #[1, 2, 3], 6
print(sum_all(5)) #[1, 2, 3, 4, 5], 15