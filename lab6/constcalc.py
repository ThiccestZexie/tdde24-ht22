from calc import *

def exec_program(program):
    if is_program(program): # Checks if the input is a valid program
        p = program_statements(program)[0]
    else:
        print("this isnt a calc program")
        return False


    if is_statements(p):
        for statement in p:
            if is_binaryexpr(statement):
                return 











    
calc1 = ['calc', ['if', [3, '>', 5], ['print', 2], ['print', 4]]]
exec_program(calc1)