from calc import *

def exec_program(program):
    if is_program(program): # Checks if the input is a valid program
        p = program_statements(program)
        return exec_statements(p)
    else:
        print("this isnt a calc program")
        return False

def exec_statements(p):

    if not empty_statements(p):
        
        exec_statement(first_statement(p))

        exec_statements(rest_statements(p))


def exec_statement(p):

    if is_statement(p):

        if is_assignment(p):
            exec_assignement(p)

        elif is_repetition(p):
            exec_repetition(p)

        elif is_selection(p):
            exec_selection(p)

        elif is_input(p):
            exec_input(p)

        elif is_output(p):
            exec_output(p)

        elif is_binaryexpr(p):
            exec_binaryexpr(p)

        elif is_condition(p):
            exec_condition(p)


def exec_assignement(p):
    1

def exec_repetition(p):
    1

def exec_selection(p):

    if exec_statement(selection_condition(p)):
        return exec_statement(selection_true_branch(p))
    elif selection_has_false_branch(p):
        return exec_statement(selection_false_branch(p))

def exec_input(p):
    1

def exec_output(p):
    print(output_expression(p))

def exec_binaryexpr(p):
    1

def exec_condition(p):
    if condition_operator(p) == '>':
        return (condition_left(p) > condition_right(p))









    
calc1 = ['calc', ['if', [3, '>', 5], ['print', 2], ['print', 4]]]
exec_program(calc1)