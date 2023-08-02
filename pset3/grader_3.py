from assignment_3 import Card, Deck, station_bikes


def print_state(description, success):
    if success:
        success="SUCCESS"
    else:
        success="FAIL"
        
    print("{:7s} {}".format(success, description))
          
def test_ex1():
    points = 0
    
    # test 1
    try:  
        card = Card("Spades", "Jack")
        points += 5
        t1 = True
    except:
        t1 = False 
    print_state("Init Card", t1)
    
    # test 2
    try:
        t2 = card.points == 10
        if t2:
            points += 5
    except:
        t2 = False
    print_state("Points for Jack of Spades", t2)
    
    # test 3
    try:
        t3 = str(card) == "Jack of Spades - 10"
        if t3:
            points += 10
    except:
        t3 = False
    print_state("__str__ for Jack of Spades", t3)
    
    # test 4
    try:
        deck1 = Deck()
        points += 5
        t4 = True
    except:
        t4 = False
    print_state("Init Deck", t4)
    
    # test 5
    try:
        first_card = deck1.pop_card()
        t5 = str(type(first_card)).endswith("Card'>")
        if t5:
            points += 10
    except:
        t5 = False  
    print_state("Deck returns a Card", t5)
    
    # test 6
    try:
        for i in range(52):
            deck1.pop_card()
        t6 = deck1.pop_card() == None
        if t6:
            points += 10
    except:
        t6 = False  
    print_state("Empty after 52 pop_card calls", t6)
        
    # test 7
    try:
        t7 = False
        for i in range(10):
            t7 = t7 or str(Deck().pop_card()) != str(Deck().pop_card())
        
        if t7:
            points += 5
    except:
        t7=False
    print_state("Shuffle", t7)
    
    return points


def test_ex2():
    points = 0
    
    # test 1
    try:  
        t1 = station_bikes("Gare do Oriente") == 40
        if t1:
            points += 25
    except:
        t1 = False 
    print_state("Bikes capacity Gare do Oriente", t1)
    
    # test 2
    try:
        t2 = station_bikes("Av. Paris / Av. Almirante Reis") == 14
        if t2:
            points += 25
    except:
        t2 = False
    print_state("Bikes capacity Av. Paris / Av. Almirante Reis", t2)
    
    
    return points

def run():
    grade = 0
    grade += test_ex1()
    print("-"*45)
    grade += test_ex2()
    print("-"*45)

    # round grade
    grade = round(grade)
    print(f"\nGrade: {grade}/100\n")

    # Warning
    print("-"*18,"WARNING","-"*18)
    warning = "This is a provisional grade, it may change.\nDifferent arguments will be used."
    print(warning)
    print("-"*45)

    return grade


if __name__ == '__main__':
    run()
