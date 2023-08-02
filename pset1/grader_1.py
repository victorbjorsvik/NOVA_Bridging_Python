import assignment_1 as work

functions = [
    work.calc_points,
    work.special_formula, 
    work.convert_eur,
    work.is_code_valid
]

ex1 = [
    ((3,6,2), 213),
    ((5,1,0), 143), 
    ((0,0,0), 0)
]

ex2 = [
    ((40,0.6), 12.7), 
    ((12,0.9), 9.6),
]

ex3 = [
    ((50,"USD"), 55.82), 
    ((50,"GBP"), 41.73), 
    ((50,"AUD"), 77.96),
    ((50,), 55.82)
]




ex4 = [
    (("aAA",), False), 
    (("aAAAAAAAAAA",), True),  
    (("abababababa",), False),
]


total_exs = [ex1,ex2,ex3,ex4]



def run(functions, total_exs):
    grade  = 0
   
    # for each exercise
    for i,exs in enumerate(total_exs):
        correct = 0
        
        # for each test case
        for inpt, outp in exs:
            print("{:35s}".format(str(functions[i].__name__)+str(inpt)), end="   ")
            
            # check if works
            try:
                if functions[i](*inpt)==outp:
                    correct+=1
                    print("SUCCESS")
                    continue
                    
            except:
                pass
            
            print("FAIL")
            
        # update grade
        grade+=correct/len(exs)/len(total_exs)
        print("-"*45)
        
    # round grade
    grade = round(grade*100)
    print(f"\nGrade: {grade}/100\n")

    # Warning
    print("-"*18,"WARNING","-"*18)
    warning = "This is a provisional grade, it may change.\nDifferent arguments will be used."
    print(warning)
    print("-"*45)
    
    return grade


if __name__ == '__main__':
    run(functions, total_exs)
    
