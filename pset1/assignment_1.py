from math import pi, sqrt, sin

def calc_points(first, second, third):
    # Calculate cumulative score for each place
    score1 = first * 25
    score2 = second * 18
    score3 = third * 15
    # Add together cumulatice scores
    sum = score1 + score2 + score3
    
    return sum


def special_formula(a, theta):
    # Define formula
    formula = sqrt(4*pi*a) * sin(theta)
    # Round Answer
    answer = round(formula, 1)
    return answer


def convert_eur(value, coin = "USD"):
    # If coin is dollar -> convert to dollar
    if coin == "USD":
        x = round( value * 1.11630, 2)
    # Else if coin is GBP -> convert to GBP
    elif coin == "GBP":
        x = round( value * 0.83463, 2)
    # Else if coin is AUD -> convert to AUD
    elif coin == "AUD":
        x = round(value * 1.55930, 2)
    # Else input is not valid - inform user
    else:
        print("Input invalid: please insert either USD, GBP or AUD")

    return x 


def is_code_valid(code):
    # Establish counters for uppercase - and lowercase letters
    count_lower = 0
    count_upper = 0
    
    # Count number of each
    for char in code:
        if char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1
    # If length less than 8 -> return False
    if len(code) < 8:
        return False
    # Else if not at least one upper and one lower -> return False
    elif count_lower == 0 or count_upper == 0:
        return False
    # All other conditions must satisfy conditions (assuming input is string) -> return True
    else:
        return True 



"""
Test your functions here
You must comment your tests when submiting your work

"""

print("calc_points")
print(calc_points(3,6,2)) #213
print(calc_points(5,1,0)) #143
print(calc_points(0,0,0)) #0

print("\nspecial_formulal")
print(special_formula(40,0.6)) #12.7
print(special_formula(12,0.9)) #9.6
print(special_formula(8,0.1)) #1.0

print("\nconvert_eur")
print(convert_eur(50,"USD")) #55.82
print(convert_eur(50,"GBP")) #41.73
print(convert_eur(50,"AUD")) #77.96
# this function should work, uncomment after you add coin as optional argument with a default value
print(convert_eur(50)) # 55.82

print("\nis_code_valid")
print(is_code_valid("aAA")) #False
print(is_code_valid("aAAAAAAAAAA")) #True
print(is_code_valid("abababababa")) #False