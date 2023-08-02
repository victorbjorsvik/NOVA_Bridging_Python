"""
Just run this file.
The content of this file should not be changed and there is no need to understand the content.
"""

import os



def read_function_from_string(function_string):
    # Create a dictionary to store the global and local variables
    global_vars = {
        "phone_book": {
            'James':218989111, 
            'Helen':910110000, 
            'Mary':910087856, 
            'Sam':900034234, 
            'Jack':219009000
        }  
    }
    local_vars = {}

    # Use exec() to execute the function string
    exec(function_string, global_vars, local_vars)

    # Get the function from the local variables
    for var_name, var_value in local_vars.items():
        if callable(var_value):
            return var_value

    raise ValueError("Function not found in the given string.")


def copy_function(source_file_path, source_function_name):
    with open(source_file_path, 'r') as source_file:
        source_code = source_file.read()

    source_function_code = ""
    inside_function = False
    lines = source_code.split('\n')
    
    imports = ""
    
    for line in lines:
        
        if line.startswith("import") or line.startswith("from "):
            imports += line + "\n"
            
        if line.strip().startswith("def " + source_function_name):
            inside_function = True
            source_function_code += line + "\n"
            
            for import_line in imports.split("\n"):
                source_function_code += "    " + import_line + "\n"
            
         
        
        elif inside_function:
            
            if len(line)>0 and line[0] != " ":
                source_function_code += "\n"
                break
            
            source_function_code += line + "\n"
    
    #print(source_function_code)
    function = read_function_from_string(source_function_code)
    
    return function


def print_state(description, success, extra):
    if success:
        success="SUCCESS"
        extra=""
    else:
        success="FAIL"
    
    message = ""
    if len(extra)>0:
        extras = extra.split("\n")
        
        message = "\n"
        for x in extras:
            line = "    "
            for i,letter in enumerate(x):
                line += letter
                
                if len(line)==45 or i+1==len(x):
                    message += line +"\n"
                    line="    "
        
    print("{:37s} {:>7} {}".format(description, success, message))


def expected(x,y):
    return "Expected {}\nGot {}".format(x,y)


def evaluate(message, points, function, expected_result):
    extra = ""
    
    try:  
        result = function()
        extra = expected(expected_result, result)
        success = result == expected_result
        if not success:
            points = 0
    except Exception as e:
        success = False 
        points = 0
        extra = expected(expected_result, "AN ERROR - "+str(e))
        
    print_state(message, success, extra)
    return points


    
def test_ex1(filename):
    
    points = 0
    
    # test 1
    def t1():
        add_contact = copy_function(filename, "add_contact")
        return add_contact("Michael",12345)
    
    points += evaluate("1.1 Add Michael", 10, t1, True)
    
    
    # test 2
    def t2():
        add_contact = copy_function(filename, "add_contact")
        add_contact("Michael",12345)
        return add_contact("Michael",12345)
    
    points += evaluate("1.2 Add Michael again", 10, t2, False)
    
    
    # test 3
    def t3():
        add_contact = copy_function(filename, "add_contact")
        return add_contact("James",12345)
    
    points += evaluate("1.3 Add James", 5, t3, False)
    
    # test 4
    def t4():
        find_phone = copy_function(filename, "find_phone")
        return find_phone("Tim")
    
    points += evaluate("1.4 Find phone Tim", 0, t4, None)
    
    # test 5
    def t5():
        find_phone = copy_function(filename, "find_phone")
        return find_phone("James")
    
    points += evaluate("1.5 Find phone James", 25, t5, 218989111)
    
    return points


def test_ex2(filename):
    points = 0
    
    # test 1
    def t1():
        sum_all = copy_function(filename, "sum_all")
        return sum_all(3)
    
    points += evaluate("2.1 sum_all(3)", 25, t1, ([1,2,3],6))
    
    
    # test 2
    def t2():
        sum_all = copy_function(filename, "sum_all")
        return sum_all(5)
    
    points += evaluate("2.2 sum_all(5)", 25, t2, ([1,2,3,4,5],15))
    
    return points


def run(filename):
    grade = 0
    
    print("-"*45)
    print(" "*18+"GRADER")
    print("-"*45)
    
    grade += test_ex1(filename)
    print("-"*45)
    grade += test_ex2(filename)
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

def is_file_in_same_folder(file_name):
    # Get the absolute path of the current script (Python file)
    script_path = os.path.abspath(__file__)

    # Extract the directory (folder) from the script path
    script_directory = os.path.dirname(script_path)

    # Join the script directory with the file name to create the full file path
    file_path = os.path.join(script_directory, file_name)

    # Check if the file exists
    return os.path.exists(file_path)


def main():
    filename = "assignment_2.py"
    
    if not is_file_in_same_folder(filename):
        folder = os.getcwd()
        print("-"*50)
        print(" "*20+"ATTENTION")
        print("-"*50)
        print(filename+" was not found in the same folder\nthan grader_1.py.\n\nPlease place assignment_1.py available on moodle\nin the following folder:\n")
        print(folder)
        
        print("\nIf it's in the correct folder, check if the file\nname was not changed and is "+filename)
        print("-"*50)
        return
        
    run(filename)
    
if __name__ == '__main__':
    main()