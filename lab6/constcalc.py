from calc import *

def exec_program(program):
    if is_program(program): # Checks if the input is a valid program
        p = program_statements(program)
        return exec_statements(p)
    else:
        print("this isnt a calc program")
        return False

def exec_statements(p):
    for statement in p:
        if not exec_statement(statement):
            return False

def exec_statement(p):
    1

def exec_assignement(p):
    1

def exec_repetition(p):
    1

def exec_selection(p):
    1

def exec_input(p):
    1

def exec_output(p):
    1

def exec_binaryexpr(p):
    1

def exec_condition(p):
    1









    
calc1 = ['calc', ['if', [3, '>', 5], ['print', 2], ['print', 4]]]
exec_program(calc1)